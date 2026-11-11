"""HOPE با نزدیکی Katz و SVD؛ نسخه‌ی مستقل NumPy
Run: python chapter_05/example_5_2_3_hope.py
Equivalent Katz/SVD construction; singular-vector signs and bases are not unique. Compare reconstructed similarity, not raw coordinates.
"""
import numpy as np
import networkx as nx
G=nx.barbell_graph(10,4);A=nx.to_numpy_array(G);beta=.01
assert beta*max(abs(np.linalg.eigvalsh(A)))<1
S=np.linalg.solve(np.eye(len(A))-beta*A,beta*A)
U,s,Vt=np.linalg.svd(S,full_matrices=False)
source=U[:,:2]*np.sqrt(s[:2]);target=Vt[:2].T*np.sqrt(s[:2])
assert np.allclose(source@target.T,(U[:,:2]*s[:2])@Vt[:2])
print('Katz low-rank error:',np.linalg.norm(S-source@target.T))

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

np.save(OUT/'source.npy',source);np.save(OUT/'target.npy',target);draw_embedding(target)
