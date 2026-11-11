"""تقسیم زمانی و ارزیابی پیش‌بینی یال بدون ورود یال‌های آینده به ورودی
Run: python chapter_08/section_8_3_13_temporal_link_evaluation.py

"""
import networkx as nx
import numpy as np
from sklearn.metrics import roc_auc_score,average_precision_score
# Synthetic dates and labels, not a real coauthorship benchmark.
events=[(0,1,1),(1,2,1),(2,3,2),(3,4,2),(4,5,2),(0,2,3),(3,5,3)]
cutoff=2;G=nx.Graph();G.add_nodes_from(range(6));G.add_edges_from((u,v) for u,v,t in events if t<=cutoff)
future={tuple(sorted((u,v))) for u,v,t in events if t>cutoff and not G.has_edge(u,v)}
candidates=sorted(nx.non_edges(G));y=np.array([tuple(sorted(e)) in future for e in candidates],dtype=int)
scores=np.array([len(list(nx.common_neighbors(G,*e))) for e in candidates])
assert all(not G.has_edge(*e) for e in future)
print('Cutoff:',cutoff,'Train edges:',list(G.edges()),'Candidates:',candidates)
print('ROC AUC:',roc_auc_score(y,scores),'Average precision:',average_precision_score(y,scores))
