"""GCN link scoring on synthetic temporal data; train graph excludes future edges."""
import numpy as np
import torch
import networkx as nx
from sklearn.metrics import roc_auc_score, average_precision_score
from torch_geometric.nn import GCNConv

torch.set_num_threads(1); torch.manual_seed(42)
rng = np.random.default_rng(42)
full = nx.stochastic_block_model([15, 15], [[.30, .04], [.04, .30]], seed=42)
all_edges = sorted(tuple(sorted(e)) for e in full.edges())
order = rng.permutation(len(all_edges))
split = int(.75 * len(order))
# Synthetic timestamps: early observed edges and a fixed future window.
early = [all_edges[i] for i in order[:split]]
future = [all_edges[i] for i in order[split:]]
G = nx.Graph(); G.add_nodes_from(range(30)); G.add_edges_from(early)
edge_index = torch.tensor(list(G.to_directed().edges()), dtype=torch.long).T
x = torch.eye(30)
nonedges = sorted(nx.non_edges(full)); rng.shuffle(nonedges)
test_negative = nonedges[:len(future)]
# Sample training nonedges from the observed graph only: future labels are not consulted.
observed_nonedges = sorted(nx.non_edges(G))
rng.shuffle(observed_nonedges)
train_negative = observed_nonedges[:len(early)]
# Some observed nonedges can become future positives: that is a temporal false-negative risk.
train_pairs = torch.tensor(early + train_negative).T
train_y = torch.tensor([1.] * len(early) + [0.] * len(train_negative))
test_pairs = torch.tensor(future + test_negative).T
test_y = np.array([1] * len(future) + [0] * len(test_negative))

class Encoder(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.first = GCNConv(30, 16)
        self.second = GCNConv(16, 8)

    def forward(self):
        return self.second(self.first(x, edge_index).relu(), edge_index)

model = Encoder(); optimizer = torch.optim.Adam(model.parameters(), lr=.01)
for _ in range(150):
    model.train(); optimizer.zero_grad(); z = model()
    logits = (z[train_pairs[0]] * z[train_pairs[1]]).sum(1)
    loss = torch.nn.functional.binary_cross_entropy_with_logits(logits, train_y)
    loss.backward(); optimizer.step()
model.eval()
with torch.no_grad():
    z = model(); scores = (z[test_pairs[0]] * z[test_pairs[1]]).sum(1).sigmoid().numpy()
assert all(not G.has_edge(*e) for e in future)
print('Synthetic future positives:', len(future))
print('ROC AUC:', roc_auc_score(test_y, scores))
print('Average precision:', average_precision_score(test_y, scores))
print('Balanced sampled test negatives; this is not population fraud/coauthorship performance.')
