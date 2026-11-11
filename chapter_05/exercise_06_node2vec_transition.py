"""تمرین ۶ فصل پنجم: نقش مستقل p در بازگشت و q در اکتشاف
Run: python chapter_05/exercise_06_node2vec_transition.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import numpy as np
# Previous t, current v; candidates: return to t, adjacent to t, distance two from t.
for p,q in [(1.,1.),(.25,1.),(1.,.25),(1.,4.)]:
    weights=np.array([1/p,1.,1/q]);print('p,q:',p,q,'candidate probabilities:',weights/weights.sum())
