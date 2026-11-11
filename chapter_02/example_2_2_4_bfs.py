"""کد کامل مثال 2.2.4: bfs
Run: python chapter_02/example_2_2_4_bfs.py
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
bfs_nodes = list(nx.bfs_tree(G, source='a').nodes())
print(bfs_nodes)
