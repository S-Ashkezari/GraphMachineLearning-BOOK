"""کد کامل مثال 5.2.2: transition_svd
Run: python chapter_05/example_5_2_2_transition_svd.py
Extracted from the book; imports, deterministic seeds, and noninteractive figure saving completed as needed.
"""
import numpy as np

# 1. Define adjacency matrix and degree matrix
A = np.array([
[0, 1, 1, 0],
[1, 0, 0, 1],
[1, 0, 0, 0],
[0, 1, 0, 0]
])

D = np.diag(A.sum(axis=1))
D_inv = np.linalg.inv(D)

# 2. Transition probability matrix
P = D_inv @ A
print("Matrix P:\n", P)

# 3. Two-step transition matrix
P2 = P @ P
print("\nMatrix P^2:\n", P2)

# 4. Singular Value Decomposition (SVD)
U1, S1, V1_T = np.linalg.svd(P)
U2, S2, V2_T = np.linalg.svd(P2)

# 5. Extract low-dimensional representations
k = 2

Y_s1 = U1[:, :k] @ np.diag(np.sqrt(S1[:k]))
Y_s2 = U2[:, :k] @ np.diag(np.sqrt(S2[:k]))

print("\nY_s^(1):\n", Y_s1)
print("\nY_s^(2):\n", Y_s2)

# 6. Concatenate embeddings
Y_s = np.hstack((Y_s1, Y_s2))

print("\nFinal Embedding Y_s:\n", Y_s)

expected_P2 = np.array([[.75,0,0,.25],[0,.75,.25,0],[0,.5,.5,0],[.5,0,0,.5]])
assert np.allclose(P2, expected_P2)
printed1 = np.array([[0,.5623],[-.5623,0],[-.9099,0],[0,.9099]])
printed2 = np.array([[-.7618,0],[0,-.7618],[0,-.6725],[-.6725,0]])
# Gram matrices remove arbitrary orthogonal choices of singular-vector basis.
assert np.allclose(Y_s1 @ Y_s1.T, printed1 @ printed1.T, atol=1e-4)
assert np.allclose(Y_s2 @ Y_s2.T, printed2 @ printed2.T, atol=1e-4)
