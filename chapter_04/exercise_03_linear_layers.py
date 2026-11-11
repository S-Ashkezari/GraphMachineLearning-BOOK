"""تمرین ۳ فصل چهارم: ترکیب لایه‌ها با بایاس، نگاشت آفین است
Run: python chapter_04/exercise_03_linear_layers.py
Computational illustration/solution; finite checks do not replace a requested general proof.
"""
import numpy as np
rng=np.random.default_rng(42);x=rng.normal(size=3);W1=rng.normal(size=(4,3));W2=rng.normal(size=(2,4));b1=rng.normal(size=4);b2=rng.normal(size=2)
assert np.allclose(W2@(W1@x+b1)+b2,(W2@W1)@x+W2@b1+b2)
print('With biases: affine map; with zero biases: linear map.')
