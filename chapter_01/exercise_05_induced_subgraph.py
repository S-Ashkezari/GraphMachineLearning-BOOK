"""تمرین ۵ فصل اول: زیرگراف القایی و غیرالقایی
Run: python chapter_01/exercise_05_induced_subgraph.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import networkx as nx
G=nx.cycle_graph(6);G.add_edge(0,2)
induced=G.subgraph([0,1,2]).copy();noninduced=induced.copy();noninduced.remove_edge(0,2)
print('Induced edges:',list(induced.edges()));print('Non-induced edges:',list(noninduced.edges()))
