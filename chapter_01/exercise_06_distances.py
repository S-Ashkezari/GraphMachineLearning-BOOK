"""تمرین ۶ فصل اول: فاصله و قطر
Run: python chapter_01/exercise_06_distances.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import networkx as nx
G=nx.path_graph(6)
print('Path 0 to 4:',nx.shortest_path(G,0,4));print('Distance:',nx.shortest_path_length(G,0,4));print('Diameter:',nx.diameter(G))
