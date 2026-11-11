"""تجمیع پیام‌های اسکالر و سهم ویژگی خود رأس
Run: python chapter_07/example_7_5_1_message_passing.py

"""
import numpy as np
A=np.array([[0,1,1],[1,0,0],[1,0,0]])
h=np.array([1.,0,0]);neighbors=A@h
print('Neighbor sum:',neighbors);print('Self + neighbor sum:',h+neighbors)
assert np.array_equal(neighbors,[0,1,1])
assert np.array_equal(h+neighbors,[1,1,1])

second = (np.eye(3)+A) @ (h+neighbors)
assert np.array_equal(second,[3,2,2]);print('Second step:',second)
