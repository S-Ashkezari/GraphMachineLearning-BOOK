"""کد کامل مثال 3.10.1: erdos_renyi
Run: python chapter_03/example_3_10_1_erdos_renyi.py
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
_figure_count += 1
plt.savefig(OUTPUT / f"figure_{_figure_count}.png", dpi=160)
plt.close()
