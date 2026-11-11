"""ماتریس‌های نمایش جبری گراف سه‌رأسی
Run: python chapter_07/example_7_2_1_laplacians.py

"""
import numpy as np
A=np.array([[0.,1,1],[1,0,0],[1,0,0]]);d=A.sum(1);D=np.diag(d);L=D-A
S=A/np.sqrt(d[:,None]*d[None,:]);Lsym=np.eye(3)-S;Lrw=np.eye(3)-A/d[:,None]
for name,value in [('A',A),('D',D),('L',L),('Lsym',Lsym),('Lrw',Lrw)]:print(name,'=\n',value)
assert np.allclose(np.linalg.eigvalsh(L),[0,1,3])
assert np.allclose(np.linalg.eigvalsh(Lsym),[0,1,2])
