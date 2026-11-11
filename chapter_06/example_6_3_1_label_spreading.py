"""تکرار و حد انتشار سخت و پخش نرم برچسب
Run: python chapter_06/example_6_3_1_label_spreading.py

"""
import numpy as np
A=np.diag(np.ones(3),1)+np.diag(np.ones(3),-1);d=A.sum(1)
P=A/d[:,None];S=A/np.sqrt(d[:,None]*d[None,:]);Y=np.array([[1.,0],[0,0],[0,0],[0,1.]])
hard=Y.copy();soft=Y.copy()
for k in range(2):
    hard=P@hard;hard[[0,3]]=Y[[0,3]];soft=.8*S@soft+.2*Y
    print('Step',k+1,'hard =\n',hard,'soft =\n',soft)
assert np.allclose(hard[1:3],[[.5,.25],[.25,.5]])
hard_limit=np.linalg.solve(np.eye(2)-P[1:3,1:3],P[1:3][:,[0,3]])
soft_limit=np.linalg.solve(np.eye(4)-.8*S,.2*Y)
assert np.allclose(hard_limit,[[2/3,1/3],[1/3,2/3]])
assert np.allclose(soft_limit,[[.343915,.084656],[.254409,.149652],[.149652,.254409],[.084656,.343915]],atol=1e-6)
print('Hard limit:\n',hard_limit);print('Soft limit:\n',soft_limit)
