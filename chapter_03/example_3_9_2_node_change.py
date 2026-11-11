"""تغییر درجه‌ی رأس و کنترل آماره‌ی ۲٫۸۶
Run: python chapter_03/example_3_9_2_node_change.py

"""
import networkx as nx
G=nx.path_graph(range(1,6));H=G.copy();H.add_edges_from([(3,1),(3,5)])
z=(H.degree(3)-2)/.7
print('Degrees:',dict(G.degree()),dict(H.degree()));print('Edges:',G.number_of_edges(),H.number_of_edges());print('z:',z)
assert G.degree(3)==2 and H.degree(3)==4 and round(z,2)==2.86
