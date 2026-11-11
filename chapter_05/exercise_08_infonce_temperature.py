"""تمرین ۸ فصل پنجم: دما در InfoNCE؛ نمونه‌ی مثبت در ستون صفر
Run: python chapter_05/exercise_08_infonce_temperature.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import numpy as np
scores=np.array([.8,.2,-.1])
for temperature in [.1,.5,1.]:
    logits=scores/temperature;logsum=logits.max()+np.log(np.exp(logits-logits.max()).sum());loss=logsum-logits[0]
    print('Temperature:',temperature,'InfoNCE loss:',loss)
