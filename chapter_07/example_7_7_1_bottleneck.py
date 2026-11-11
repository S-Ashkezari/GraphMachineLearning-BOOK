"""رشد درخت‌ها در دو سوی گلوگاه؛ نمونه‌ی ساختاری
Run: python chapter_07/example_7_7_1_bottleneck.py

"""
import networkx as nx
for depth in range(1,6):
    left=nx.balanced_tree(2,depth);right=nx.balanced_tree(2,depth)
    G=nx.disjoint_union(left,right);n=len(left);G.add_node(2*n);G.add_edges_from([(0,2*n),(n,2*n)])
    print('Depth',depth,'two trees nodes',2*n,'fixed representation dimension',8)
    assert nx.is_articulation_point(G,2*n) if hasattr(nx,'is_articulation_point') else 2*n in set(nx.articulation_points(G))
# Counting growth illustrates the bottleneck; it is not a proof of information loss for every learned model.
