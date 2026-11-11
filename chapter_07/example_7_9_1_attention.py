"""ضریب توجه بزرگ‌تر لزوماً سهم برداری بزرگ‌تر نیست؛ پارامترهای مفروض
Run: python chapter_07/example_7_9_1_attention.py

"""
import numpy as np
scores=np.array([2.,1.]);a=np.exp(scores-scores.max());a/=a.sum()
messages=np.array([[.1,0],[0,10.]])
print('Attention:',a);print('Weighted contributions:',a[:,None]*messages)
assert a[0]>a[1] and np.linalg.norm(a[0]*messages[0])<np.linalg.norm(a[1]*messages[1])
print('Output:',a@messages)
