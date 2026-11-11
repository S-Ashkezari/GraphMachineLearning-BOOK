"""نمایش عکس‌لحظه‌ای؛ داده‌ی مصنوعی آموزشی
Run: python chapter_03/example_3_4_1_snapshots.py

"""
import networkx as nx
# Illustrative interactions: the book specifies the representation, not a measured dataset.
daily=[[(0,1),(1,2)],[(0,2),(2,3)],[(0,1),(0,3)]]
for day,edges in enumerate(daily,1):
    G=nx.Graph();G.add_nodes_from(range(4));G.add_edges_from(edges)
    print('Day',day,'edges',list(G.edges()),'degrees',dict(G.degree()))
