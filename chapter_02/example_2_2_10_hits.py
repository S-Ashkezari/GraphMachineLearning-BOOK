"""سه تکرار و حد HITS؛ کنترل نتایج متن
Run: python chapter_02/example_2_2_10_hits.py

"""
"""Reproduce and verify the book's three HITS iterations; requires NumPy."""
import numpy as np

vertices = ("P", "Q", "R", "S", "T", "U")
edges = (("P", "R"), ("P", "S"), ("Q", "R"), ("Q", "S"),
         ("T", "R"), ("U", "R"))
A = np.zeros((6, 6))
for source, target in edges:
    A[vertices.index(source), vertices.index(target)] = 1

expected = [((4, 2), (6, 6, 4, 4)),
            ((20, 12), (32, 32, 20, 20)),
            ((104, 64), (168, 168, 104, 104))]
h = np.ones(6)
print("Vertex order:", vertices)
for step, (authority, hub) in enumerate(expected, 1):
    a = A.T @ h
    a /= np.linalg.norm(a)
    h = A @ a
    h /= np.linalg.norm(h)
    expected_a = np.zeros(6)
    expected_h = np.zeros(6)
    expected_a[[2, 3]] = np.asarray(authority) / np.linalg.norm(authority)
    expected_h[[0, 1, 4, 5]] = np.asarray(hub) / np.linalg.norm(hub)
    np.testing.assert_allclose(a, expected_a, rtol=1e-12, atol=1e-12)
    np.testing.assert_allclose(h, expected_h, rtol=1e-12, atol=1e-12)
    assert a[2] > a[3] and h[0] == h[1] and h[0] > h[4] == h[5]
    print(f"Iteration {step}: authority={a.round(6)}, hub={h.round(6)}")
print("All three iterations and stated rankings verified.")
