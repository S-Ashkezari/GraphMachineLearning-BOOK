"""پشتیبانی تراکنشی یک کمان در سه گراف
Run: python chapter_02/example_2_5_1_transactional_support.py

"""
import networkx as nx
graphs=[nx.DiGraph([(0,1),(1,2)]),nx.DiGraph([(0,1),(0,2)]),nx.DiGraph([(0,1),(1,2),(2,0)])]
pattern=nx.DiGraph([(0,1)])
support=sum(nx.algorithms.isomorphism.DiGraphMatcher(g,pattern).subgraph_is_monomorphic() for g in graphs)
assert support==3
print('Support:',support,'Relative support:',support/len(graphs))
