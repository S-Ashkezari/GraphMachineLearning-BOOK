"""تمرین ۱۵ فصل سوم: مقایسه‌ی اجتماع‌ها؛ برای ژیروان–نیومن نخستین تقسیم گزارش می‌شود
Run: python chapter_03/exercise_15_community_comparison.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
G=nx.barabasi_albert_graph(30,2,seed=42)
parts={'Louvain':nx.community.louvain_communities(G,seed=42),'Label propagation':list(nx.community.asyn_lpa_communities(G,seed=42)),'Girvan-Newman first split':list(next(nx.community.girvan_newman(G)))}
pos=nx.spring_layout(G,seed=42);fig,axes=plt.subplots(1,3,figsize=(15,4))
for ax,(name,groups) in zip(axes,parts.items()):
    labels={v:k for k,group in enumerate(groups) for v in group}
    print(name,len(groups),'modularity',nx.community.modularity(G,groups))
    nx.draw(G,pos,ax=ax,node_color=[labels[v] for v in G],with_labels=True,node_size=150);ax.set_title(name)
out=Path(__file__).parent/'outputs';out.mkdir(exist_ok=True);fig.savefig(out/'exercise_15_communities.png',dpi=160)
