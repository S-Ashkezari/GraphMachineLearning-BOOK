"""عملگرهای ساخت بازنمایی یال
Run: python chapter_05/section_5_2_6_edge_operators.py

"""
import numpy as np
x=np.array([1.,2,3]);y=np.array([3.,1,2])
for name,value in [('average',(x+y)/2),('Hadamard',x*y),('weighted L1',abs(x-y)),('weighted L2',(x-y)**2),('concatenation',np.r_[x,y])]:print(name,value)
