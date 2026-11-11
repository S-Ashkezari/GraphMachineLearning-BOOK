"""فاکتورگیری آموزشیِ یال‌های مشاهده‌شده با منظم‌سازی؛ نسخه‌ی مستقل NumPy
Run: python chapter_05/example_5_2_1_graph_factorization.py
The book GEM call is archived in docs/original-listings.md. This implementation optimizes the stated symmetric observed-edge objective, not GEM software internals. Coordinates depend on initialization.
"""
import numpy as np
import networkx as nx
G=nx.barbell_graph(10,4);A=nx.to_numpy_array(G);mask=A>0
rng=np.random.default_rng(42);Y=rng.normal(0,.01,(24,2));reg=1.;eta=1e-4
def objective(Y):
    return .25*np.sum(((A-Y@Y.T)*mask)**2)+.5*reg*np.sum(Y**2)
before=objective(Y)
for _ in range(10000):
    residual=(Y@Y.T-A)*mask
    Y-=eta*(residual@Y+reg*Y)
after=objective(Y)
assert after<before
print('Observed-edge GF objective:',before,after)
print('Clique node IDs: 0..9 and 14..23; bridge: 10..13')

from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
OUT=Path(__file__).resolve().parent/'outputs'/Path(__file__).stem
OUT.mkdir(parents=True,exist_ok=True)
def draw_embedding(Y):
    fig,(left,ax)=plt.subplots(1,2,figsize=(12,5))
    nx.draw(G,nx.spring_layout(G,seed=42),ax=left,with_labels=True,node_size=110,font_size=7,node_color='white',edgecolors='black')
    left.set_title('Barbell graph')
    ax.set_title('Embedding')
    for ids,marker in [(range(10),'o'),(range(10,14),'^'),(range(14,24),'s')]:
        ids=list(ids);ax.scatter(Y[ids,0],Y[ids,1],marker=marker,facecolors='none',edgecolors='black')
        if len(ids)>4:
            label='0-9' if ids[0]==0 else '14-23'
            ax.annotate(label,Y[ids].mean(axis=0),xytext=(8,8),textcoords='offset points',fontsize=9)
        else:
            for i in ids:ax.annotate(str(i),Y[i,:2],xytext=(4,4),textcoords='offset points',fontsize=8)
    ax.margins(.2)
    fig.tight_layout();fig.savefig(OUT/'embedding.png',dpi=180);plt.close(fig)

np.save(OUT/'embedding.npy',Y);draw_embedding(Y)
