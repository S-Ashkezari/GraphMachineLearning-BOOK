"""زیان تک‌نمونه‌ای، MSE، انتروپی متقاطع و گرادیان
Run: python chapter_04/section_4_2_2_loss_and_sgd.py

"""
import numpy as np
X=np.array([[1.,0],[1,1],[1,2]]);y=np.array([1.,3,5]);theta=np.zeros(2)
loss=(y-X@theta)**2;full_gradient=2*X.T@(X@theta-y)/len(y)
sample_gradients=2*X*(X@theta-y)[:,None]
assert np.allclose(full_gradient,sample_gradients.mean(0))
for step in range(200):theta-=.05*(2*X.T@(X@theta-y)/len(y))
print('Single losses:',loss,'MSE:',loss.mean(),'Fitted theta:',theta)
prob=np.array([[.8,.2],[.1,.9]]);classes=np.array([0,1])
print('Cross entropy per sample:',-np.log(prob[np.arange(2),classes]))
