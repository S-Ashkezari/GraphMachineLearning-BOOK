"""کد کامل مثال 2.2.7: dijkstra
Run: python chapter_02/example_2_2_7_dijkstra.py
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
# Run Dijkstra's algorithm from a source node
# This function returns a dictionary where:
# distances[v] is the shortest distance from source to v
distances = nx.single_source_dijkstra_path_length(G, source='a')

# Print shortest distances from source node 'a'
for node in distances:
    print(f"Shortest distance from a to {node} = {distances[node]}")
