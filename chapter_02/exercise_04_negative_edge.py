"""تمرین ۴ فصل دوم: علت شکست دایکسترا با یال منفی
Run: python chapter_02/exercise_04_negative_edge.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import networkx as nx
import heapq
G=nx.DiGraph();G.add_weighted_edges_from([('s','a',1),('s','b',2),('b','a',-3)])
# Deliberately label-setting Dijkstra: finalized vertices cannot be improved.
dist={'s':0};done=set();q=[(0,'s')]
while q:
    d,u=heapq.heappop(q)
    if u in done:continue
    done.add(u)
    for v,data in G[u].items():
        if v not in done and d+data['weight']<dist.get(v,float('inf')):
            dist[v]=d+data['weight'];heapq.heappush(q,(dist[v],v))
correct=nx.single_source_bellman_ford_path_length(G,'s')
print('Label-setting result:',dist);print('Bellman-Ford:',correct)
assert dist['a']==1 and correct['a']==-1
