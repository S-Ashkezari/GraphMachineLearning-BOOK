"""تمرین ۷ فصل دوم: چهار درخت پوشای کمینه
Run: python chapter_02/exercise_07_multiple_msts.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import networkx as nx
from itertools import combinations
G=nx.cycle_graph(4);trees=[]
for edges in combinations(G.edges(),3):
    T=nx.Graph();T.add_nodes_from(G);T.add_edges_from(edges)
    if nx.is_tree(T):trees.append(edges)
print('Equal-weight spanning trees:',trees);assert len(trees)==4
