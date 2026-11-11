"""خودشبکه‌ی کاهش‌یافته؛ حذف ساختاری برگ‌ها و حفظ جهت و وزن
Run: python chapter_08/section_8_1_4_reduced_egonet.py

"""
import networkx as nx
G=nx.DiGraph();G.add_weighted_edges_from([('A','B',100),('B','C',100),('C','A',100),('A','D',1),('A','E',1)])
center='A';nodes={center}|set(G.predecessors(center))|set(G.successors(center))
ego=G.subgraph(nodes).copy();undirected=ego.to_undirected()
keep={center}|{v for v in ego if v!=center and any(u!=center for u in undirected[v])}
reduced=ego.subgraph(keep).copy()
print('Egonet:',sorted(ego),'density:',nx.density(ego));print('Reduced:',sorted(reduced),'density:',nx.density(reduced))
assert set(reduced)==set('ABC') and reduced['A']['B']['weight']==100
