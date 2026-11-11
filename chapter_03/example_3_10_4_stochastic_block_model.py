"""کد کامل مثال 3.10.4: stochastic_block_model
Run: python chapter_03/example_3_10_4_stochastic_block_model.py
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
plt.savefig(OUTPUT / "sbm_network_shapes.png", dpi=300)
_figure_count += 1
plt.savefig(OUTPUT / f"figure_{_figure_count}.png", dpi=160)
plt.close()
