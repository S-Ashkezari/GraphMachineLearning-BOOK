"""دو ترتیب مجاز BFS با صف صریح
Run: python chapter_02/example_2_2_3_bfs_orders.py

"""
import networkx as nx
edges=[('a','b'),('a','c'),('b','d'),('b','e'),('c','f'),('d','i'),('e','j'),('f','g'),('f','h'),('i','j')]
G=nx.Graph(edges)

from collections import deque
def bfs(reverse=False):
    queue=deque(['a']);seen={'a'};out=[]
    while queue:
        v=queue.popleft();out.append(v)
        for w in sorted(G[v],reverse=reverse):
            if w not in seen:seen.add(w);queue.append(w)
    return out
print(bfs());print(bfs(True))
assert bfs()==list('abcdefijgh')
assert bfs(True)==list('acbfedhgji')
