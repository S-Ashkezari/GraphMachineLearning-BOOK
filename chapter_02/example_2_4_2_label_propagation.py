"""کد کامل مثال 2.4.2: label_propagation
Run: python chapter_02/example_2_4_2_label_propagation.py
Extracted from the book; imports, deterministic seeds, and noninteractive figure saving completed as needed.
"""
import networkx as nx
G = nx.Graph()
edges = [(1,2),(1,3),(2,3),(3,4),(4,5)]
G.add_edges_from(edges)
# Run label propagation algorithm
communities = nx.algorithms.community.label_propagation_communities(G)
print("Communities:")
for comm in communities:
    print(list(comm))
