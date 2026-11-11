"""تمرین ۲ فصل سوم: مسیر ایستا و نامعتبر بودن ترتیب زمانی
Run: python chapter_03/exercise_02_temporal_path.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import networkx as nx
events=[('A','B',3),('B','C',1)]
static=nx.DiGraph((u,v) for u,v,t in events);arrival={'A':0}
for u,v,t in sorted(events,key=lambda e:e[2]):
    if arrival.get(u,float('inf'))<=t:arrival[v]=t
print('Static path:',nx.shortest_path(static,'A','C'));print('Temporal arrival:',arrival)
assert nx.has_path(static,'A','C') and 'C' not in arrival
