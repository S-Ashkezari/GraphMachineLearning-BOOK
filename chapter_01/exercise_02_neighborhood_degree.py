"""تمرین ۲ فصل اول: همسایگی و درجه
Run: python chapter_01/exercise_02_neighborhood_degree.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import networkx as nx
G=nx.Graph([('a','b'),('a','c'),('a','d'),('b','c')])
print('Open:',sorted(G['a']));print('Closed:',sorted(set(G['a'])|{'a'}))
print('Degree(a), delta, Delta:',G.degree('a'),min(dict(G.degree()).values()),max(dict(G.degree()).values()))
assert G.degree('a')==3
