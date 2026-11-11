"""گراف دوبخشی کامل K4,2
Run: python chapter_01/example_1_2_1_complete_bipartite.py

"""
import networkx as nx
G=nx.complete_bipartite_graph(4,2)
G=nx.relabel_nodes(G,dict(enumerate('uvwxyz')))
print('X:',list('uvwx'),'Y:',list('yz'))
print('Edges:',sorted(G.edges()))
assert G.number_of_edges()==8 and nx.is_bipartite(G)
