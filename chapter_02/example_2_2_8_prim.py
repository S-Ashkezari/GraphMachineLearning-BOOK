"""کد کامل مثال 2.2.8: prim
Run: python chapter_02/example_2_2_8_prim.py
Extracted from the book; imports, deterministic seeds, and noninteractive figure saving completed as needed.
"""
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
