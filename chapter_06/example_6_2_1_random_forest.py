"""کد کامل مثال 6.2.1: random_forest
Run: python chapter_06/example_6_2_1_random_forest.py
Extracted from the book; imports, deterministic seeds, and noninteractive figure saving completed as needed.
"""
import networkx as nx
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# 1. Load the observed karate club network
G = nx.karate_club_graph()
# Use only the unweighted topology in this example.
nx.set_edge_attributes(G, 1.0, 'weight')
# Pre-calculate global graph metrics for efficiency Centrality measures
deg_centrality = nx.degree_centrality(G)
bet_centrality = nx.betweenness_centrality(G)
close_centrality = nx.closeness_centrality(G)
eig_centrality = nx.eigenvector_centrality(G)
pagerank = nx.pagerank(G)
# 2. Feature Extraction
features = []
labels = []
for node in G.nodes():
    # Basic Structural Features
    degree = G.degree(node)
    clustering = nx.clustering(G, node)
    # Centrality Features
    d_cent = deg_centrality[node]
    b_cent = bet_centrality[node]
    c_cent = close_centrality[node]
    e_cent = eig_centrality[node]
    p_rank = pagerank[node]
    # Number of triangles the node participates in
    triangles = nx.triangles(G, node)
    # Average degree of the node's neighbors
    neighbor_degrees = [G.degree(n) for n in G.neighbors(node)]
    avg_neighbor_deg = np.mean(neighbor_degrees) if neighbor_degrees else 0
    # Concatenate all features into a single vector
    feature_vector = [
        degree, clustering, d_cent, b_cent, c_cent, e_cent, p_rank, triangles, avg_neighbor_deg ]
    features.append(feature_vector)
    # Target label
    labels.append(0 if G.nodes[node]['club'] == 'Mr. Hi' else 1)
# Convert to numpy arrays
X = np.array(features)
y = np.array(labels)
# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
# 4. Classification
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)
# 5. Evaluation
y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
