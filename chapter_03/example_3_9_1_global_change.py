"""تغییر سراسری؛ مقیاس تنظیم‌شده‌ی ۱، نه انحراف معیار تجربی پنجره‌ی ثابت
Run: python chapter_03/example_3_9_1_global_change.py

"""
import networkx as nx
import numpy as np
G=nx.Graph([(1,2),(2,3),(4,5)]);H=G.copy();H.add_edges_from([(1,3),(2,4),(3,4),(3,5)])
past=np.array([3.,3.]);sigma_floor=1.0
z=(H.number_of_edges()-past.mean())/max(past.std(),sigma_floor)
assert G.number_of_edges()==3 and H.number_of_edges()==7 and z==4
print('Edges before/after:',G.number_of_edges(),H.number_of_edges(),'regularized z:',z)
