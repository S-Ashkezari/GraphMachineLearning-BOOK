"""بردار ویژه و چندجمله‌ای مشخصه؛ مثال تکمیلی
Run: python chapter_01/section_1_4_linear_algebra.py

"""
import numpy as np
A=np.array([[2.,1.],[1.,2.]])
values,vectors=np.linalg.eigh(A)
print('Eigenvalues:',values);print('Eigenvectors (columns):\n',vectors)
print('Characteristic polynomial coefficients:',np.poly(A))
assert np.allclose(A@vectors,vectors*values)
assert np.allclose(np.poly(A),[1,-4,3])
