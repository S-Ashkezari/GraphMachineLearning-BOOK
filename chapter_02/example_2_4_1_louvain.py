"""کد کامل مثال 2.4.1: louvain
Run: python chapter_02/example_2_4_1_louvain.py
Extracted from the book; imports, deterministic seeds, and noninteractive figure saving completed as needed.
"""
import networkx as nx
import community as community_louvain
# Create graph
G = nx.Graph()
edges = [(1,2),(1,3),(2,3),(3,4),(4,5)]
G.add_edges_from(edges)
# Run Louvain
partition = community_louvain.best_partition(G, random_state=42)
print("Communities:")
for node, comm in partition.items():
    print(f"Node {node}: Community {comm}")
