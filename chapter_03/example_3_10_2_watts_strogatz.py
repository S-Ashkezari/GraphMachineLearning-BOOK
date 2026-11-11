"""کد کامل مثال 3.10.2: watts_strogatz
Run: python chapter_03/example_3_10_2_watts_strogatz.py
Extracted from the book; imports, deterministic seeds, and noninteractive figure saving completed as needed.
"""
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
OUTPUT = Path(__file__).resolve().parent / "outputs" / Path(__file__).stem
OUTPUT.mkdir(parents=True, exist_ok=True)
_figure_count = 0
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
_figure_count += 1
plt.savefig(OUTPUT / f"figure_{_figure_count}.png", dpi=160)
plt.close()
