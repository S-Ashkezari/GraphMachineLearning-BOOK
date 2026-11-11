"""تمرین ۱۰ فصل هفتم: حد انتشار با وزن درجه
Run: python chapter_07/exercise_10_oversmoothing.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import numpy as np
import networkx as nx
A=nx.to_numpy_array(nx.path_graph(5))+np.eye(5);d=A.sum(1);P=A/d[:,None];pi=d/d.sum()
H=np.arange(10.).reshape(5,2);limit=np.ones((5,1))@(pi@H)[None,:]
for k in [1,5,25,200]:print('Step',k,'distance to limit',np.linalg.norm(np.linalg.matrix_power(P,k)@H-limit))
assert np.allclose(np.linalg.matrix_power(P,200)@H,limit)
