"""محاسبه‌ی عددی لایه‌ی پیچشی و بیشینه‌تجمیع؛ داده‌ی تکمیلی
Run: python chapter_04/section_4_4_1_convolution_pooling.py

"""
import numpy as np
X=np.arange(1,17).reshape(4,4);kernel=np.array([[1,0],[0,-1]])
out=np.array([[np.sum(X[i:i+2,j:j+2]*kernel) for j in range(3)] for i in range(3)])
pool=np.array([[X[i:i+2,j:j+2].max() for j in [0,2]] for i in [0,2]])
print('Input:',X,sep=chr(10));print('Cross-correlation used in CNNs:',out,sep=chr(10));print('Max pool:',pool,sep=chr(10))
assert out.shape==(3,3) and np.array_equal(pool,[[6,8],[14,16]])
