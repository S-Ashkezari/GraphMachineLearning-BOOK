"""مسیر، دور جهت‌دار و گراف بدون دور؛ نمونه‌ی محاسباتی
Run: python chapter_01/example_1_2_4_paths_cycles_dag.py

"""
import networkx as nx
path=nx.path_graph(4,create_using=nx.DiGraph)
cycle=nx.cycle_graph(4,create_using=nx.DiGraph)
print('Directed path:',nx.shortest_path(path,0,3))
print('Directed cycle:',list(nx.simple_cycles(cycle)))
print('Path is DAG:',nx.is_directed_acyclic_graph(path))
assert not nx.is_directed_acyclic_graph(cycle)
