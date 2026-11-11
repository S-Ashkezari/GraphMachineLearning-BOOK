"""تمرین ۲ فصل هفتم: انتشار حرارت و کاهش انرژی
Run: python chapter_07/exercise_02_heat_diffusion.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import numpy as np
import networkx as nx
from scipy.linalg import expm
A=nx.to_numpy_array(nx.path_graph(5));L=np.diag(A.sum(1))-A;values,U=np.linalg.eigh(L);x=np.array([1.,0,0,0,0])
for t in [0.,.1,1.,10.]:
    y=U@(np.exp(-t*values)*(U.T@x));assert np.allclose(y,expm(-t*L)@x)
    print('t:',t,'signal:',y,'energy:',y@L@y)
