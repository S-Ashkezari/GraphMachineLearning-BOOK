"""تمرین ۳ فصل سوم: میانگین متحرک بدون استفاده از آینده
Run: python chapter_03/exercise_03_moving_average.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import numpy as np
counts=np.array([3,4,3,4,3,12,4]);window=4
for t in range(window,len(counts)):
    past=counts[t-window:t];z=(counts[t]-past.mean())/max(past.std(),1.)
    print('t:',t,'past mean:',past.mean(),'z:',z,'alarm:',abs(z)>3)
