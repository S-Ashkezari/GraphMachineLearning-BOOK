"""تمرین ۷ فصل چهارم: MRR و Hits@k روی رتبه‌های معلوم
Run: python chapter_04/exercise_07_ranking_metrics.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import numpy as np
ranks=np.array([1,3,5]);print('Reciprocal ranks:',1/ranks,'MRR:',np.mean(1/ranks))
for k in [1,3,5]:print(f'Hits@{k}:',np.mean(ranks<=k))
