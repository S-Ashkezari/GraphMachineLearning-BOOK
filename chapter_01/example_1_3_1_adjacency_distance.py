"""تطبیق ماتریس مجاورت، فاصله و ترتیب رأس‌های مثال ۱-۳-۱
Run: python chapter_01/example_1_3_1_adjacency_distance.py

"""
import numpy as np
import networkx as nx
nodes=list('uvwxy')
G=nx.DiGraph();G.add_nodes_from(nodes)
G.add_edges_from([('u','v'),('u','w'),('v','u'),('w','x'),('x','v'),('x','y'),('y','x')])
A=nx.to_numpy_array(G,nodelist=nodes,dtype=int)
D=np.asarray(nx.floyd_warshall_numpy(G,nodelist=nodes))
expected=np.array([[0,1,1,2,3],[1,0,2,3,4],[3,2,0,1,2],[2,1,3,0,1],[3,2,4,1,0]])
assert np.array_equal(D,expected)
print('Row/column order:',nodes);print('A =\n',A);print('D =\n',D.astype(int))
for v in nodes:print(v,':',list(G.successors(v)))
