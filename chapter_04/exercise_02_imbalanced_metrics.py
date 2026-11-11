"""تمرین ۲ فصل چهارم: دقت بالا و بازیابی صفر
Run: python chapter_04/exercise_02_imbalanced_metrics.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import numpy as np
from sklearn.metrics import accuracy_score,recall_score,precision_score,confusion_matrix
y=np.r_[np.zeros(990,dtype=int),np.ones(10,dtype=int)];pred=np.zeros_like(y)
print('Confusion:',confusion_matrix(y,pred));print('Accuracy:',accuracy_score(y,pred),'Recall:',recall_score(y,pred),'Precision:',precision_score(y,pred,zero_division=0))
assert accuracy_score(y,pred)==.99 and recall_score(y,pred)==0
