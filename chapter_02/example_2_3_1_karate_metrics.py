"""کد کامل مثال 2.3.1: karate_metrics
Run: python chapter_02/example_2_3_1_karate_metrics.py
Extracted from the book; imports, deterministic seeds, and noninteractive figure saving completed as needed.
"""
import networkx as nx
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
OUTPUT = Path(__file__).resolve().parent / "outputs" / Path(__file__).stem
OUTPUT.mkdir(parents=True, exist_ok=True)
_figure_count = 0
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
_figure_count += 1
plt.savefig(OUTPUT / f"figure_{_figure_count}.png", dpi=160)
plt.close()
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

assert round(metrics['Characteristic Path Length'],2)==2.41
assert round(metrics['Transitivity'],2)==.26
assert round(metrics['Modularity'],2)==.41
assert round(metrics['Degree Assortativity'],2)==-.48
