"""تمرین ۲ فصل ششم: یک گام انتشار با مرز ثابت
Run: python chapter_06/exercise_02_six_node_propagation.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import numpy as np
import networkx as nx
A=nx.to_numpy_array(nx.path_graph(6));P=A/A.sum(1)[:,None];Y=np.zeros((6,2));Y[0,0]=1;Y[-1,1]=1
F=P@Y;F[[0,-1]]=Y[[0,-1]];print('Initial:',Y,'One clamped step:',F)
assert np.allclose(F[1],[.5,0]) and np.allclose(F[-2],[0,.5])
