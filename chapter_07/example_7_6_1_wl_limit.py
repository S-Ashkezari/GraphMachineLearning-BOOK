"""ناتوانی WL-1 در تفکیک C6 و دو مثلث؛ واژگان رنگ مشترک
Run: python chapter_07/example_7_6_1_wl_limit.py

"""
import networkx as nx
from collections import Counter
graphs=[nx.cycle_graph(6),nx.disjoint_union(nx.cycle_graph(3),nx.cycle_graph(3))]
colors=[{v:0 for v in g} for g in graphs]
for step in range(3):
    keys=[{v:(c[v],tuple(sorted(c[u] for u in g[v]))) for v in g} for g,c in zip(graphs,colors)]
    vocabulary={key:i for i,key in enumerate(sorted({x for k in keys for x in k.values()}))}
    colors=[{v:vocabulary[key] for v,key in k.items()} for k in keys]
    hist=[Counter(c.values()) for c in colors];print(step+1,hist);assert hist[0]==hist[1]
assert not nx.is_isomorphic(*graphs)
