"""حالت پنهان RNN با پارامترهای معلوم؛ مثال تکمیلی
Run: python chapter_04/section_4_5_1_recurrent_state.py

"""
import numpy as np
Wx=np.array([[.4],[-.2]]);Wh=np.array([[.5,.1],[.2,.3]]);b=np.zeros(2);h=np.zeros(2)
for x in [1.,0.,-1.,.5]:
    h=np.tanh(Wx[:,0]*x+Wh@h+b);print('x:',x,'hidden:',h)
assert np.max(abs(h))<=1
