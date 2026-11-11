"""مقایسه‌ی یال و کمان؛ داده‌ی کوچک آموزشی مطابق مفهوم مثال
Run: python chapter_01/example_1_2_3_directed_undirected.py

"""
import networkx as nx
G=nx.Graph([('u','v'),('v','w'),('u','w')])
D=nx.DiGraph([('u','v'),('v','w'),('w','u')])
print('Undirected edges:',list(G.edges()))
print('Directed arcs:',list(D.edges()))
print('Reverse adjacency v->u:',G.has_edge('v','u'),D.has_edge('v','u'))
