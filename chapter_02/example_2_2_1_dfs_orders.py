"""ترتیب‌های DFS با تعیین صریح ترتیب همسایه‌ها
Run: python chapter_02/example_2_2_1_dfs_orders.py

"""
import networkx as nx
edges=[('a','b'),('a','c'),('b','d'),('b','e'),('c','f'),('d','i'),('e','j'),('f','g'),('f','h'),('i','j')]
G=nx.Graph(edges)

def dfs(order):
    seen=set();out=[]
    def visit(v):
        seen.add(v);out.append(v)
        for w in order[v]:
            if w not in seen:visit(w)
    visit('a');return out
ascending={v:sorted(G[v]) for v in G}
descending={v:sorted(G[v],reverse=True) for v in G}
first=dfs(ascending);second=dfs(descending)
print(first);print(second)
assert first==list('abdijecfgh')
assert second==list('acfhgbejid')
