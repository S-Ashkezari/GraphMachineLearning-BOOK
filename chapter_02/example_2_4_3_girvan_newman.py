"""کد کامل مثال 2.4.3: girvan_newman
Run: python chapter_02/example_2_4_3_girvan_newman.py
Extracted from the book; imports, deterministic seeds, and noninteractive figure saving completed as needed.
"""
import networkx as nx
from networkx.algorithms import community
G = nx.Graph()
edges = [(1,2),(1,3),(2,3),(3,4),(4,5)]
G.add_edges_from(edges)
# Run Girvan-Newman
comp = community.girvan_newman(G)
limited = tuple(sorted(c) for c in next(comp))
print("Communities:")
for c in limited:
    print(c)
