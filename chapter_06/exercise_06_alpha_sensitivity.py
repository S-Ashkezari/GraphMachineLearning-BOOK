"""تمرین ۶ فصل ششم: حساسیت پخش نرم به آلفا
Run: python chapter_06/exercise_06_alpha_sensitivity.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import numpy as np
import networkx as nx
A=nx.to_numpy_array(nx.path_graph(6));d=A.sum(1);S=A/np.sqrt(d[:,None]*d[None,:]);Y=np.zeros((6,2));Y[0,0]=1;Y[-1,1]=1
for alpha in [0.,.2,.8,.99]:
    F=np.linalg.solve(np.eye(6)-alpha*S,(1-alpha)*Y)
    print('Alpha:',alpha,'scores:',F,'labels:',F.argmax(1))
