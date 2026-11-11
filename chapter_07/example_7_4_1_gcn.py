"""کد کامل مثال 7.4.1: gcn
Run: python chapter_07/example_7_4_1_gcn.py
Extracted from the book; imports, deterministic seeds, and noninteractive figure saving completed as needed.
"""
import torch
import torch.nn.functional as F
from torch_geometric.datasets import KarateClub
from torch_geometric.nn import GCNConv

class GCN(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super().__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, out_channels)

    def forward(self, x, edge_index):
        x = F.relu(self.conv1(x, edge_index))
        return self.conv2(x, edge_index)

torch.set_num_threads(1)
torch.manual_seed(42)
dataset = KarateClub()
data = dataset[0]
n = data.num_nodes
order = torch.randperm(n)
cut = int(0.8 * n)
train_mask = torch.zeros(n, dtype=torch.bool)
test_mask = torch.zeros(n, dtype=torch.bool)
train_mask[order[:cut]] = True
test_mask[order[cut:]] = True
model = GCN(dataset.num_features, 32, dataset.num_classes)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01,
                             weight_decay=5e-4)
criterion = torch.nn.CrossEntropyLoss()
for epoch in range(200):
    model.train()
    optimizer.zero_grad()
    logits = model(data.x, data.edge_index)
    loss = criterion(logits[train_mask], data.y[train_mask])
    loss.backward()
    optimizer.step()
model.eval()
with torch.no_grad():
    pred = model(data.x, data.edge_index).argmax(dim=1)
    accuracy = (pred[test_mask] == data.y[test_mask]).float().mean()
print(f"Test accuracy: {accuracy.item():.4f}")
