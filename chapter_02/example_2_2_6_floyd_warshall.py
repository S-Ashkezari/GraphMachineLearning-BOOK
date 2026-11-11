"""کد کامل مثال 2.2.6: floyd_warshall
Run: python chapter_02/example_2_2_6_floyd_warshall.py
Extracted from the book; imports, deterministic seeds, and noninteractive figure saving completed as needed.
"""
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
