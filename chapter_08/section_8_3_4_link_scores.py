"""امتیازهای همسایگی مشترک، ژاکارد و آدامیک–آدار برای مثال هشت پژوهشگر
Run: python chapter_08/section_8_3_4_link_scores.py

"""
import networkx as nx
import numpy as np
neighbors={'A':'BCD','B':'ACE','C':'ABDE','D':'ACF','E':'BCFG','F':'DEG','G':'EFH','H':'G'}
G=nx.Graph();G.add_nodes_from(neighbors)
G.add_edges_from((v,u) for v,adj in neighbors.items() for u in adj)
rows=[]
for u,v in sorted(nx.non_edges(G)):
    common=len(list(nx.common_neighbors(G,u,v)));jaccard=next(nx.jaccard_coefficient(G,[(u,v)]))[2];aa=next(nx.adamic_adar_index(G,[(u,v)]))[2]
    rows.append((u,v,common,jaccard,aa))
for row in sorted(rows,key=lambda r:(-r[2],r[0],r[1])):print(row)
row=next(r for r in rows if r[:2]==('A','E'));assert row[2]==2 and row[3]==.4 and np.isclose(row[4],1/np.log(3)+1/np.log(4))
