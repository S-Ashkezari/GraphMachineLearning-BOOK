"""تفاوت جمع و میانگین؛ نمونه‌ی نقض تزریقی‌بودن عمومی جمع
Run: python chapter_07/example_7_6_2_sum_mean.py

"""
import numpy as np
a=np.ones(2);b=np.ones(3)
print('Means:',a.mean(),b.mean());print('Sums:',a.sum(),b.sum())
assert a.mean()==b.mean() and a.sum()!=b.sum()
print('Counterexample to general injectivity of sum:',sum([1,3]),sum([2,2]))
