"""تمرین ۱۶ فصل هفتم: ساخت دو نما و زوج‌های مثبت
Run: python chapter_07/exercise_16_contrastive_views.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import numpy as np
import networkx as nx
rng=np.random.default_rng(42);G=nx.cycle_graph(8);random_view=G.copy()
random_view.remove_edges_from([e for e in G.edges() if rng.random()<.25])
deterministic_view=G.subgraph(range(6)).copy()
print('Random edge-drop view:',list(random_view.edges()));print('Induced view:',list(deterministic_view.edges()))
print('Positive node pairs:',[(v,v) for v in deterministic_view]);print('Negatives: distinct node IDs, subject to false-negative caveat.')
