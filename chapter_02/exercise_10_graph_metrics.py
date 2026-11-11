"""تمرین ۱۰ فصل دوم: شاخص‌های گراف شش‌رأسی
Run: python chapter_02/exercise_10_graph_metrics.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import networkx as nx
G=nx.cycle_graph(6)
print('Degrees:',dict(G.degree()));print('Mean distance:',nx.average_shortest_path_length(G));print('Diameter:',nx.diameter(G))
assert nx.diameter(G)==3
