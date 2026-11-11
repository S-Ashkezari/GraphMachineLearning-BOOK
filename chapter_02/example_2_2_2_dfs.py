"""کد کامل مثال 2.2.2: dfs
Run: python chapter_02/example_2_2_2_dfs.py
Extracted from the book; imports, deterministic seeds, and noninteractive figure saving completed as needed.
"""
import networkx as nx
edges = [
('a', 'b'), ('a', 'c'),
('b', 'd'), ('b', 'e'),
('c', 'f'),
('d', 'i'),
('e', 'j'),
('f', 'g'), ('f', 'h'),
('i', 'j')
]
G = nx.Graph()
G.add_edges_from(edges)
dfs_nodes = list(nx.dfs_preorder_nodes(G, source='a'))
print(dfs_nodes)
