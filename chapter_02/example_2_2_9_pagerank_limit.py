"""چهار تکرار و حد PageRank؛ کنترل برتری C بر A
Run: python chapter_02/example_2_2_9_pagerank_limit.py

"""
import numpy as np
import networkx as nx
nodes=list('ABCDE');G=nx.DiGraph();G.add_nodes_from(nodes)
G.add_edges_from([('A','B'),('A','C'),('B','C'),('C','A'),('D','C'),('E','C')])
A=nx.to_numpy_array(G,nodelist=nodes);P=A/A.sum(1)[:,None]
p=np.ones(5)/5
for k in range(4):
    p=.03+.85*P.T@p;print(k+1,dict(zip(nodes,p.round(8))));assert np.isclose(p.sum(),1)
limit=np.linalg.solve(np.eye(5)-.85*P.T,np.full(5,.03))
print('Limit:',dict(zip(nodes,limit)));print('C-A:',limit[2]-limit[0])
assert limit[2]>limit[0]
assert np.allclose(limit,list(nx.pagerank(G,alpha=.85,tol=1e-13).values()))

assert np.allclose(limit, [.363369,.184432,.392199,.03,.03],atol=5e-7)
assert np.allclose(p, [.384689,.138030,.417281,.03,.03],atol=5e-7)
