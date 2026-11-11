# کادرهای کد نسخه‌ی مبنا

این کادرها برای ردیابی تغییرات نگهداری شده‌اند؛ نسخه‌های کامل قابل اجرا در پوشه‌های فصل‌ها قرار دارند.

## مثال 2.2.2

```python
import networkx as nx
edges = [
('a', 'b'), ('a', 'c'),
('b', 'd'), ('b', 'e'),
('c', 'f'),
('d', 'i'),
('e', 'j'),
('f', 'g'), ('f', 'h'),
('i', 'j')
]
G = nx.Graph()
G.add_edges_from(edges)
dfs_nodes = list(nx.dfs_preorder_nodes(G, source='a'))
print(dfs_nodes)
```

## مثال 2.2.4

```python
import networkx as nx
edges = [
('a', 'b'), ('a', 'c'),
('b', 'd'), ('b', 'e'),
('c', 'f'),
('d', 'i'),
('e', 'j'),
('f', 'g'), ('f', 'h'),
('i', 'j')
]
G = nx.Graph()
G.add_edges_from(edges)
bfs_nodes = list(nx.bfs_tree(G, source='a').nodes())
print(bfs_nodes)
```

## مثال 2.2.6

```python
import networkx as nx
# Create a weighted graph
G = nx.Graph()
# Add weighted edges (u, v, weight)
edges = [
('a', 'b', 3),
('a', 'c', 1),
('b', 'c', 7),
('b', 'd', 5),
('c', 'd', 2)
]
G.add_weighted_edges_from(edges)
# Run the Floyd–Warshall algorithm
# The result is a dictionary of dictionaries:
# distances[u][v] gives the shortest distance from u to v
distances = nx.floyd_warshall(G)
for u in distances:
    for v in distances[u]:
        print(f"Shortest distance from {u} to {v} = {distances[u][v]}")
```

## مثال 2.2.7

```python
import networkx as nx
# Create a weighted graph
G = nx.Graph()
# Add weighted edges (u, v, weight)
edges = [
    ('a', 'b', 3),
    ('a', 'c', 1),
    ('b', 'c', 7),
    ('b', 'd', 5),
    ('c', 'd', 2)
]
G.add_weighted_edges_from(edges)
# Run Dijkstra's algorithm from a source node
# This function returns a dictionary where:
# distances[v] is the shortest distance from source to v
distances = nx.single_source_dijkstra_path_length(G, source='a')

# Print shortest distances from source node 'a'
for node in distances:
    print(f"Shortest distance from a to {node} = {distances[node]}")
```

## مثال 2.2.8

```python
import networkx as nx
# Create a weighted, undirected graph
G = nx.Graph()
# Add weighted edges (u, v, weight)
edges = [
('a', 'b', 3),
('a', 'c', 1),
('b', 'c', 7),
('b', 'd', 5),
('c', 'd', 2)
]
G.add_weighted_edges_from(edges)
# Run Prim's algorithm
# NetworkX provides a built-in function to compute the MST
mst = nx.minimum_spanning_tree(G, algorithm='prim')
# Print edges of the Minimum Spanning Tree
print("Edges in the Minimum Spanning Tree:")
for u, v, data in mst.edges(data=True):
    print(f"{u} -- {v}  (weight = {data['weight']})")
```

## مثال 2.3.1

```python
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
# Load the Karate Club graph
G = nx.karate_club_graph()
# Draw the graph
plt.figure(figsize=(6,6))
pos = nx.spring_layout(G, seed=42)
nx.draw(
G, pos,
with_labels=True,
node_size=500,
node_color="lightgray",
edge_color="gray"
)
plt.title("Karate Club Graph")
plt.show()
# Compute graph metrics
metrics = {
    "Characteristic Path Length":
    nx.average_shortest_path_length(G),
    "Global Efficiency":
    nx.global_efficiency(G),
    "Local Efficiency":
    nx.local_efficiency(G),
    "Average Clustering":
    nx.average_clustering(G),
    "Transitivity":
    nx.transitivity(G),
    "Modularity":
    nx.community.modularity(
    G,
    nx.community.greedy_modularity_communities(G)
    ),
    "Degree Assortativity":
    nx.degree_assortativity_coefficient(G)
}
# Store results in a table
df = pd.DataFrame(
metrics.items(),
columns=["Metric", "Value"]
)
print(df)
```

## مثال 2.4.1

```python
import networkx as nx
import community as community_louvain
# Create graph
G = nx.Graph()
edges = [(1,2),(1,3),(2,3),(3,4),(4,5)]
G.add_edges_from(edges)
# Run Louvain
partition = community_louvain.best_partition(G)
print("Communities:")
for node, comm in partition.items():
    print(f"Node {node}: Community {comm}")
```

## مثال 2.4.2

```python
import networkx as nx
G = nx.Graph()
edges = [(1,2),(1,3),(2,3),(3,4),(4,5)]
G.add_edges_from(edges)
# Run label propagation algorithm
communities = nx.algorithms.community.label_propagation_communities(G)
print("Communities:")
for comm in communities:
    print(list(comm))
```

## مثال 2.4.3

```python
import networkx as nx
from networkx.algorithms import community
G = nx.Graph()
edges = [(1,2),(1,3),(2,3),(3,4),(4,5)]
G.add_edges_from(edges)
# Run Girvan-Newman
comp = community.girvan_newman(G)
limited = tuple(sorted(c) for c in next(comp))
print("Communities:")
for c in limited:
    print(c)
```

## مثال 3.10.1

```python
import networkx as nx
import matplotlib.pyplot as plt
# Parameters
n = 20
p = 1.5 / n   # slightly above critical threshold 1/n
# Generate ER graph
G = nx.erdos_renyi_graph(n, p, seed=42)
# Layout (nodes slightly closer)
pos = nx.spring_layout(G, k=0.3, seed=42)
# Draw graph
plt.figure(figsize=(6,6))
nx.draw(G, pos,
with_labels=True,
node_color='skyblue',
edge_color='gray',
node_size=400)
    
plt.title("Erdős–Rényi Graph G(n,p)")
plt.box(True)  # add box around plot
plt.show()
```

## مثال 3.10.2

```python
import networkx as nx
import matplotlib.pyplot as plt
# =========================
# Parameters
# =========================
n = 20      # number of nodes
k = 4       # each node connected to k nearest neighbors (must be even)
p = 0.2     # rewiring probability
# =========================
# Generate Watts–Strogatz graph
# =========================
G = nx.watts_strogatz_graph(n, k, p, seed=42)
# =========================
# Compute structural metrics
# =========================
clustering = nx.average_clustering(G)
# Ensure graph is connected before computing average shortest path
if nx.is_connected(G):
    path_length = nx.average_shortest_path_length(G)
else:
    # Report path length on the largest component only.
    largest_cc = max(nx.connected_components(G), key=len)
    G_sub = G.subgraph(largest_cc)
    path_length = nx.average_shortest_path_length(G_sub)
    print("Path length uses largest component:", len(largest_cc))
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("Average clustering coefficient:", round(clustering, 4))
print("Average shortest path length:", round(path_length, 4))
# =========================
# Visualization
# =========================
plt.figure(figsize=(6,6))
# Circular layout shows small-world structure clearly
pos = nx.circular_layout(G)
nx.draw(G,pos,with_labels=True,node_size=500,node_color='lightblue', edge_color='gray'
)
plt.title(f"Watts–Strogatz Model (n={n}, k={k}, p={p})", fontsize=12)
plt.tight_layout()
plt.show()
```

## مثال 3.10.3

```python
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
# =========================
# Parameters
# =========================
n = 100   # number of nodes
m = 2     # edges per new node
# =========================
# Generate BA graph
# =========================
G = nx.barabasi_albert_graph(n, m, seed=42)
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("Average degree:", sum(dict(G.degree()).values())/n)
# =========================
# Plot network
# =========================
plt.figure(figsize=(6,6))
pos = nx.spring_layout(G, k=0.3, seed=42)
nx.draw(G, pos, node_size=50, node_color='lightblue', edge_color='gray')
plt.title("Barabási–Albert Network")
plt.tight_layout()
plt.savefig("ba_network.png", dpi=300)
plt.show()
# =========================
# Degree distribution
# =========================
degrees = [d for _, d in G.degree()]
unique_deg = sorted(set(degrees))
counts = [degrees.count(k) for k in unique_deg]
plt.figure(figsize=(6,4))
plt.loglog(unique_deg, counts, 'o')
plt.xlabel("Degree k")
plt.ylabel("Frequency")
plt.title("Degree Distribution (log-log scale)")
plt.tight_layout()
plt.savefig("ba_degree_distribution.png", dpi=300)
plt.show()
```

## مثال 3.10.4

```python
import networkx as nx
import matplotlib.pyplot as plt
# =========================
# Parameters
# =========================
sizes = [30, 30]   # sizes of communities
p = [[0.4, 0.01],
[0.01, 0.4]]  # probability matrix
# =========================
# Generate SBM graph
# =========================
G = nx.stochastic_block_model(sizes, p, seed=42)
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
# =========================
# Layout
# =========================
pos = nx.spring_layout(G, seed=42)
# Separate nodes by community (block attribute)
community0 = [n for n, d in G.nodes(data=True) if d["block"] == 0]
community1 = [n for n, d in G.nodes(data=True) if d["block"] == 1]
# =========================
# Draw graph
# =========================
plt.figure(figsize=(6,6))
# Draw edges first
nx.draw_networkx_edges(G, pos, edge_color='gray', alpha=0.5)
# Draw community 0 as circles
nx.draw_networkx_nodes(
G, pos,
nodelist=community0,
node_shape='o',       # circle
node_color='lightgray',
edgecolors='black',
node_size=80,
label="Community 1")
# Draw community 1 as squares
nx.draw_networkx_nodes(
G, pos,
nodelist=community1,
node_shape='s',       # square
node_color='white',
edgecolors='black',
node_size=80,
label="Community 2")
plt.title("Stochastic Block Model (Shape-coded Communities)")
plt.legend()
plt.axis("off")
plt.tight_layout()
plt.savefig("sbm_network_shapes.png", dpi=300)
plt.show()
```

## مثال 5.2.1

```python
import networkx as nx
#!pip install git+https://github.com/palash1992/GEM.git
from gem.embedding.gf import GraphFactorization
import matplotlib.pyplot as plt
            
G = nx.barbell_graph(m1=10, m2=4)

gf = GraphFactorization(d=2,  data_set=None,max_iter=10000, eta=1*10**-4, regu=1.0)
gf.learn_embedding(G)
            
fig, ax = plt.subplots(figsize=(5,5))
            
for x in G.nodes():
            
    v = gf.get_embedding()[x]
    ax.scatter(v[0],v[1], s=1000)
    ax.annotate(str(x), (v[0],v[1]), fontsize=12)
```

## مثال 5.2.2

```python
import numpy as np
            
# 1. Define adjacency matrix and degree matrix
A = np.array([
[0, 1, 1, 0],
[1, 0, 0, 1],
[1, 0, 0, 0],
[0, 1, 0, 0]
])
            
D = np.diag(A.sum(axis=1))
D_inv = np.linalg.inv(D)
    
# 2. Transition probability matrix
P = D_inv @ A
print("Matrix P:\n", P)
    
# 3. Two-step transition matrix
P2 = P @ P
print("\nMatrix P^2:\n", P2)
            
# 4. Singular Value Decomposition (SVD)
U1, S1, V1_T = np.linalg.svd(P)
U2, S2, V2_T = np.linalg.svd(P2)
            
# 5. Extract low-dimensional representations
k = 2
        
Y_s1 = U1[:, :k] @ np.diag(np.sqrt(S1[:k]))
Y_s2 = U2[:, :k] @ np.diag(np.sqrt(S2[:k]))
            
print("\nY_s^(1):\n", Y_s1)
print("\nY_s^(2):\n", Y_s2)
            
# 6. Concatenate embeddings
Y_s = np.hstack((Y_s1, Y_s2))
            
print("\nFinal Embedding Y_s:\n", Y_s)
```

## مثال 5.2.3

```python
import networkx as nx
import matplotlib.pyplot as plt
from gem.embedding.hope import HOPE
            
G = nx.barbell_graph(m1=10, m2=4)
    
hp = HOPE(d=4, beta=0.01)
hp.learn_embedding(G)
            
fig, ax = plt.subplots(figsize=(5,5))
            
for x in G.nodes():
    v = hp.get_embedding()[x,2:]
    ax.scatter(v[0],v[1], s=1000)
    ax.annotate(str(x), (v[0],v[1]), fontsize=20)
```

## مثال 5.2.4

```python
import networkx as nx
import matplotlib.pyplot as plt
from node2vec import Node2Vec
            
G = nx.barbell_graph(m1=10, m2=4)
draw_graph(G)
                
node2vec = Node2Vec(G, dimensions=2)
model = node2vec.fit(window=10)
embeddings = model.wv
            
fig, ax = plt.subplots(figsize=(7,7))
                
for x in G.nodes():
    v = model.wv[str(x)]
    ax.scatter(v[0],v[1], s=1000)
    ax.annotate(str(x), (v[0],v[1]), fontsize=12)
plt.show()
```

## مثال 6.2.1

```python
import networkx as nx
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# 1. Load the observed karate club network
G = nx.karate_club_graph()
# Use only the unweighted topology in this example.
nx.set_edge_attributes(G, 1.0, 'weight')
# Pre-calculate global graph metrics for efficiency Centrality measures
deg_centrality = nx.degree_centrality(G)
bet_centrality = nx.betweenness_centrality(G)
close_centrality = nx.closeness_centrality(G)
eig_centrality = nx.eigenvector_centrality(G)
pagerank = nx.pagerank(G)
# 2. Feature Extraction
features = []
labels = []
for node in G.nodes():
    # Basic Structural Features
    degree = G.degree(node)
    clustering = nx.clustering(G, node)
    # Centrality Features
    d_cent = deg_centrality[node]
    b_cent = bet_centrality[node]
    c_cent = close_centrality[node]
    e_cent = eig_centrality[node]
    p_rank = pagerank[node]
    # Number of triangles the node participates in
    triangles = nx.triangles(G, node)
    # Average degree of the node's neighbors
    neighbor_degrees = [G.degree(n) for n in G.neighbors(node)]
    avg_neighbor_deg = np.mean(neighbor_degrees) if neighbor_degrees else 0
    # Concatenate all features into a single vector
    feature_vector = [
        degree, clustering, d_cent, b_cent, c_cent, e_cent, p_rank, triangles, avg_neighbor_deg ]
    features.append(feature_vector)
    # Target label
    labels.append(0 if G.nodes[node]['club'] == 'Mr. Hi' else 1)
# Convert to numpy arrays
X = np.array(features)
y = np.array(labels)
# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
# 4. Classification
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)
# 5. Evaluation
y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
```

## مثال 7.4.1

```python
class GCN(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super(GCN, self).__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, out_channels)
            
    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        return x
```

## مثال 7.5.2

```python
class MPNN(MessagePassing):
    def __init__(self, in_channels, out_channels):
        super().__init__(aggr='add')
        self.lin = torch.nn.Linear(in_channels, out_channels)
        
    def forward(self, x, edge_index):
        return self.lin(self.propagate(edge_index, x=x))
                
    def message(self, x_j):
        return x_j
            
# Load dataset
torch.manual_seed(42)
dataset = KarateClub()
data = dataset[0]
order = torch.randperm(data.num_nodes)
cut = int(0.8 * data.num_nodes)
train_mask = torch.zeros(data.num_nodes, dtype=torch.bool)
train_mask[order[:cut]] = True

model = MPNN(dataset.num_features, dataset.num_classes)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01,
                             weight_decay=5e-4)
criterion = torch.nn.CrossEntropyLoss()
        
# Training loop
for epoch in range(200):
    model.train()
    optimizer.zero_grad()
    out = model(data.x, data.edge_index)
    loss = criterion(out[train_mask], data.y[train_mask])
    loss.backward()
    optimizer.step()
```
