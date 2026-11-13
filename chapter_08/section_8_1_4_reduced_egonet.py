"""خودشبکه‌ی کاهش‌یافته؛ حذف ساختاری برگ‌ها و حفظ جهت و وزن
Run: python chapter_08/section_8_1_4_reduced_egonet.py

"""
import networkx as nx
G=nx.DiGraph();G.add_weighted_edges_from([('A','B',100),('B','C',100),('C','A',100),('A','D',1),('A','E',1)])
center='A';nodes={center}|set(G.predecessors(center))|set(G.successors(center))
ego=G.subgraph(nodes).copy()
# Count incoming and outgoing arcs: reciprocal arcs to the center count twice.
# This retains the reciprocal neighbor shown in the source paper's Example 1.
keep={center}|{v for v in ego if v!=center and ego.degree(v)>1}
reduced=ego.subgraph(keep).copy()
print('Egonet:',sorted(ego),'density:',nx.density(ego));print('Reduced:',sorted(reduced),'density:',nx.density(reduced))
assert set(reduced)==set('ABC') and reduced['A']['B']['weight']==100

# A two-way neighbor must survive even if its only distinct neighbor is A.
reciprocal=nx.DiGraph([('A','R'),('R','A'),('A','L')])
retained={'A'}|{v for v in reciprocal if v!='A' and reciprocal.degree(v)>1}
assert retained=={'A','R'}
