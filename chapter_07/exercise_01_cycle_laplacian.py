"""تمرین ۱ فصل هفتم: لاپلاسین چرخه‌ی چهارتایی
Run: python chapter_07/exercise_01_cycle_laplacian.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import numpy as np
import networkx as nx
A=nx.to_numpy_array(nx.cycle_graph(4));D=np.diag(A.sum(1));L=D-A;Lsym=L/2
for name,M in [('A',A),('D',D),('L',L),('Lsym',Lsym)]:print(name,'\n',M)
assert np.allclose(np.linalg.eigvalsh(Lsym),[0,1,1,2])
