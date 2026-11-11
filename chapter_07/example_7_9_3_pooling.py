"""تجمیع سلسله‌مراتبی با ماتریس تخصیص مفروض
Run: python chapter_07/example_7_9_3_pooling.py

"""
import numpy as np
import networkx as nx
G=nx.Graph([(0,1),(1,2),(0,2),(2,3),(3,4),(4,5),(3,5)])
A=nx.to_numpy_array(G,nodelist=range(6));X=np.arange(12.).reshape(6,2)
S=np.zeros((6,2));S[:3,0]=1;S[3:,1]=1
print('Pooled adjacency:\n',S.T@A@S);print('Pooled features:\n',S.T@X)
assert np.array_equal(S.T@A@S,[[6,1],[1,6]])
# Diagonal counts within-group directed adjacency entries (each undirected edge twice).
