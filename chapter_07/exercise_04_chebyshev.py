"""تمرین ۴ فصل هفتم: بازه‌ی طیفی و بازگشت چبیشف
Run: python chapter_07/exercise_04_chebyshev.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import numpy as np
import networkx as nx
A=nx.to_numpy_array(nx.path_graph(5));L=np.diag(A.sum(1))-A;largest=np.linalg.eigvalsh(L)[-1]
scaled=2*L/largest-np.eye(5);values=np.linalg.eigvalsh(scaled)
assert values.min()>=-1-1e-12 and values.max()<=1+1e-12
x=np.arange(5.);T0=x;T1=scaled@x;T2=2*scaled@T1-T0
print('Rescaled spectrum:',values,'T2 x:',T2)
