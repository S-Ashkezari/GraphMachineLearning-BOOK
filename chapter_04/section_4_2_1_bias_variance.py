"""بازتولید عددی نمودار بایاس–واریانس کتاب؛ سبک خطوط قابل تشخیص در چاپ سیاه‌وسفید
Run: python chapter_04/section_4_2_1_bias_variance.py

"""
import numpy as np
from numpy.polynomial.legendre import legvander
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
rng=np.random.default_rng(20261105);sigma=.2;n=25;x=np.linspace(-1,1,n);grid=np.linspace(-1,1,501)
truth=lambda t:1.2*t-1.5*t**3;y=truth(x)+rng.normal(0,sigma,n)
fig,axes=plt.subplots(3,1,figsize=(8,10));metrics={}
for ax,degree in zip(axes,[1,3,11]):
    A=legvander(x,degree);B=legvander(grid,degree);pinv=np.linalg.pinv(A);S=B@pinv
    mean=S@truth(x);prediction=S@y;sd=sigma*np.sqrt((S*S).sum(1))
    bias=np.mean((mean-truth(grid))**2);variance=np.mean(sd**2)
    train=np.mean((A@pinv@truth(x)-truth(x))**2)+sigma**2*(1-(degree+1)/n)
    test=bias+variance+sigma**2
    metrics[str(degree)]=dict(expected_train_mse=float(train),expected_test_mse=float(test),bias_squared=float(bias),variance=float(variance),noise_variance=sigma**2)
    ax.plot(grid,truth(grid),'k--',label='True function');ax.plot(grid,mean,'k:',label='Mean model');ax.plot(grid,prediction,'k-',linewidth=.7,label='One fit')
    ax.fill_between(grid,mean-sd,mean+sd,color='.85',label='One standard deviation');ax.scatter(x,y,s=8,c='black');ax.set_ylim(-1.25,1.25);ax.set_title(f'Degree {degree}');ax.legend(fontsize=7)
expected={1:(.101,.097),3:(.034,.046),11:(.021,.059)}
for d,(train,test) in expected.items():assert round(metrics[str(d)]['expected_train_mse'],3)==train and round(metrics[str(d)]['expected_test_mse'],3)==test
out=Path(__file__).parent/'outputs';out.mkdir(exist_ok=True);fig.tight_layout();fig.savefig(out/'bias_variance.png',dpi=180)
(out/'bias_variance_metrics.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8');print(json.dumps(metrics,indent=2))
