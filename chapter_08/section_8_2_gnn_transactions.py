"""Synthetic transaction-node classification; not a real fraud detection benchmark."""
import numpy as np
import torch
import networkx as nx
from sklearn.metrics import average_precision_score, confusion_matrix
from torch_geometric.nn import GCNConv

torch.set_num_threads(1)
torch.manual_seed(42)
rng = np.random.default_rng(42)
G = nx.stochastic_block_model([40, 20], [[.14, .03], [.03, .20]], seed=42)
# Synthetic binary labels and noisy account attributes; no real customer data.
y = torch.tensor([0] * 40 + [1] * 20)
attributes = rng.normal(size=(60, 4))
attributes[40:, 0] += .8
x = torch.tensor(attributes, dtype=torch.float32)
edge_index = torch.tensor(list(G.to_directed().edges()), dtype=torch.long).T
train, test = [], []
for label in [0, 1]:
    ids = rng.permutation(np.flatnonzero(y.numpy() == label))
    train.extend(ids[:int(.7 * len(ids))]); test.extend(ids[int(.7 * len(ids)):])
train, test = torch.tensor(train), torch.tensor(test)
# Fit preprocessing on training attributes only.
x = (x - x[train].mean(0)) / x[train].std(0).clamp_min(1e-6)

class Classifier(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.first = GCNConv(4, 16)
        self.second = GCNConv(16, 2)

    def forward(self):
        return self.second(self.first(x, edge_index).relu(), edge_index)

model = Classifier()
optimizer = torch.optim.Adam(model.parameters(), lr=.01, weight_decay=5e-4)
for _ in range(100):
    model.train(); optimizer.zero_grad()
    loss = torch.nn.functional.cross_entropy(model()[train], y[train])
    loss.backward(); optimizer.step()
model.eval()
with torch.no_grad():
    probability = model().softmax(1)[test, 1].numpy()
truth = y[test].numpy()
print('Synthetic held-out nodes:', test.tolist())
print('Average precision:', average_precision_score(truth, probability))
print('Confusion matrix at fixed 0.5 threshold:', confusion_matrix(truth, probability >= .5))
print('Transductive observed topology; held-out labels never used for fitting.')
