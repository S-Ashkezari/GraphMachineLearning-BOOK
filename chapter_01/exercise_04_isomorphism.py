"""تمرین ۴ فصل اول: یک‌ریختی و نگاشت
Run: python chapter_01/exercise_04_isomorphism.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import networkx as nx
G=nx.cycle_graph(4);H=nx.relabel_nodes(G,{0:2,1:0,2:3,3:1})
matcher=nx.algorithms.isomorphism.GraphMatcher(G,H)
assert matcher.is_isomorphic();print('Isomorphism:',matcher.mapping)
print('C4 isomorphic to path P4:',nx.is_isomorphic(G,nx.path_graph(4)))
