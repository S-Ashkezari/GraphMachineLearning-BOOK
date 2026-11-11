"""تمرین ۱ فصل پنجم: تمایز تقریب کم‌رتبه‌ی آزاد و فاکتورگیری نیمه‌معین مثبت
Run: python chapter_05/exercise_01_psd_factorization.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import numpy as np
A=np.array([[0.,1],[1,0]])
values,U=np.linalg.eigh(A);positive=values>0;Y=U[:,positive]*np.sqrt(values[positive])
print('Eigenvalues:',values,'PSD approximation:',Y@Y.T,'error:',np.linalg.norm(A-Y@Y.T))
assert np.isclose(np.linalg.norm(A-Y@Y.T),1)
print('YY^T is PSD; unrestricted truncated SVD and PSD factorization are different constraints.')
