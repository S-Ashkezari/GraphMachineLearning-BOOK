"""کنترل دقیق مثلث‌های مثال: چهار مثلث، نه فقط دو مثلث
Run: python chapter_03/example_3_9_3_triangle_change.py

"""
import networkx as nx
from itertools import combinations
G=nx.path_graph(range(1,7));H=G.copy();H.add_edges_from([(1,3),(2,4),(4,6),(3,6)])
triangles=[t for t in combinations(H.nodes(),3) if all(H.has_edge(u,v) for u,v in combinations(t,2))]
print('Triangles before:',sum(nx.triangles(G).values())//3)
print('Triangles after:',triangles)
assert triangles==[(1,2,3),(2,3,4),(3,4,6),(4,5,6)]
