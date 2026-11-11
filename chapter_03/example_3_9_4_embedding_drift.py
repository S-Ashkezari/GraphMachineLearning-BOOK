"""فاصله‌ی دو بازنمایی مفروض و هم‌تراز
Run: python chapter_03/example_3_9_4_embedding_drift.py

"""
import numpy as np
z1=np.array([.2,.3]);z2=np.array([.8,.9]);distance=np.linalg.norm(z2-z1)
print('Distance:',distance,'Above threshold:',distance>.5)
assert round(distance,2)==.85
# Coordinates are the assumed, aligned embeddings in the book, not independently trained models.
