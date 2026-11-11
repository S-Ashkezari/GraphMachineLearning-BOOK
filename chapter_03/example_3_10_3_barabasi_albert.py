"""کد کامل مثال 3.10.3: barabasi_albert
Run: python chapter_03/example_3_10_3_barabasi_albert.py
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
plt.savefig(OUTPUT / "ba_network.png", dpi=300)
_figure_count += 1
plt.savefig(OUTPUT / f"figure_{_figure_count}.png", dpi=160)
plt.close()
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
plt.savefig(OUTPUT / "ba_degree_distribution.png", dpi=300)
_figure_count += 1
plt.savefig(OUTPUT / f"figure_{_figure_count}.png", dpi=160)
plt.close()
