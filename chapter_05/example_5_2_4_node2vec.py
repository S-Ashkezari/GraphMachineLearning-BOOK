"""کد کامل مثال 5.2.4: node2vec
Run: python chapter_05/example_5_2_4_node2vec.py
Extracted from the book; imports, deterministic seeds, and noninteractive figure saving completed as needed.
"""
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
OUTPUT = Path(__file__).resolve().parent / "outputs" / Path(__file__).stem
OUTPUT.mkdir(parents=True, exist_ok=True)
from node2vec import Node2Vec

G = nx.barbell_graph(m1=10, m2=4)
nx.draw(G, nx.spring_layout(G, seed=42), with_labels=True)
plt.savefig(OUTPUT / "graph.png", dpi=160)
plt.close()

node2vec = Node2Vec(G, dimensions=2, seed=42, workers=1, quiet=True)
model = node2vec.fit(window=10, min_count=1, seed=42, epochs=20)
embeddings = model.wv

fig, ax = plt.subplots(figsize=(7,7))

for ids,marker,label in [(list(range(10)),'o','0-9'),(list(range(10,14)),'^','10-13'),(list(range(14,24)),'s','14-23')]:
    coordinates = [model.wv[str(i)] for i in ids]
    ax.scatter([v[0] for v in coordinates],[v[1] for v in coordinates],s=45,marker=marker,facecolors='none',edgecolors='black',label=label)
    if len(ids)==4:
        for i,v in zip(ids,coordinates):ax.annotate(str(i),v,xytext=(4,4),textcoords='offset points',fontsize=9)
ax.legend(title='Node IDs');ax.margins(.15);fig.tight_layout()
plt.savefig(OUTPUT / 'embedding.png', dpi=180)
plt.close()
