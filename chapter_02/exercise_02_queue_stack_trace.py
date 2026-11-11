"""تمرین ۲ فصل دوم: وضعیت صف و پشته
Run: python chapter_02/exercise_02_queue_stack_trace.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
from collections import deque
adj={0:[1,2],1:[3,4],2:[5,6],3:[],4:[],5:[],6:[]}
queue=deque([0]);seen={0}
while queue:
    print('BFS queue before pop:',list(queue));v=queue.popleft()
    for u in adj[v]:
        if u not in seen:seen.add(u);queue.append(u)
stack=[0];seen=set()
while stack:
    print('DFS stack before pop:',stack);v=stack.pop()
    if v in seen:continue
    seen.add(v);stack.extend(reversed(adj[v]))
