"""Reproducible vector figure: fixed-design polynomial regression, Gaussian noise.
Run from the book directory. Requires numpy, reportlab, XeLaTeX and the XB Yas font.
"""
from pathlib import Path
import json
import subprocess
import shutil
import numpy as np
from numpy.polynomial.legendre import legvander
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color

BASE=Path(__file__).resolve().parents[1]/'chapter_04'/'outputs'/'persian_figure'
BASE.mkdir(parents=True,exist_ok=True)
OUT=BASE
rng=np.random.default_rng(20261105)
n=25; sigma=.20
x=np.linspace(-1,1,n); grid=np.linspace(-1,1,501)
truth=lambda t: 1.2*t-1.5*t**3
y=truth(x)+rng.normal(0,sigma,n)
W,H=480,610
c=canvas.Canvas(str(OUT/'bias-variance-base.pdf'),pagesize=(W,H))
c.setTitle('Bias and variance on a known regression function')
blue=HexColor('#23658C'); orange=HexColor('#B94D12'); ink=HexColor('#20252B')
left,right=53,465; pw=right-left
ylow,yhigh=-1.25,1.25
metrics={}
labels=[]
def fa(x,y,s,size=10,color=ink):
    rgb=','.join(f'{v:.4f}' for v in (color.red,color.green,color.blue))
    labels.append(r'\node[anchor=base east,inner sep=0pt,text={rgb,1:red,'+str(color.red)+';green,'+str(color.green)+';blue,'+str(color.blue)+r'},font=\fontsize{'+str(size)+'}{'+str(size*1.3)+r'}\selectfont] at ('+f'{x:.3f},{y:.3f}'+') {\\rl{'+s+'}};')
def num(v):
    return str(v).translate(str.maketrans('0123456789.','۰۱۲۳۴۵۶۷۸۹٫'))

def text(x,y,s,size=9,color=ink):
    c.setFillColor(color); c.setFont('Helvetica',size); c.drawString(x,y,s)
def line(points,color,width=1,dash=None):
    c.setStrokeColor(color); c.setLineWidth(width); c.setDash(dash or [])
    p=c.beginPath(); p.moveTo(*points[0])
    for a,b in points[1:]:p.lineTo(a,b)
    c.drawPath(p)
    c.setDash([])
for k,(degree,title) in enumerate([(1,'الف) کم‌برازش: بایاس زیاد'),(3,'ب) برازش مناسب در این مثال'),(11,'ج) بیش‌برازش: واریانس زیاد')]):
    bottom=430-k*185; height=125
    xx=lambda t:left+(np.asarray(t)+1)*pw/2
    yy=lambda t:bottom+(np.asarray(t)-ylow)*height/(yhigh-ylow)
    A=legvander(x,degree); B=legvander(grid,degree); pinv=np.linalg.pinv(A)
    S=B@pinv
    mean=S@truth(x); pred=S@y; sd=sigma*np.sqrt((S*S).sum(axis=1))
    bias2=np.mean((mean-truth(grid))**2); var=np.mean(sd**2)
    train=np.mean((A@pinv@truth(x)-truth(x))**2)+sigma**2*(1-(degree+1)/n)
    test=bias2+var+sigma**2
    metrics[str(degree)]={'expected_train_mse':float(train),'expected_test_mse':float(test),'bias_squared':float(bias2),'variance':float(var),'noise_variance':sigma**2}
    fa(right,bottom+height+26,title,13)
    fa(right,bottom+height+11,'درجه‌ی '+num(degree)+'؛ میانگین خطای مربعی مورد انتظار: آموزش '+num(f'{train:.3f}')+'، آزمون '+num(f'{test:.3f}'),10)
    for val in [-1,0,1]:
        line([(left,yy(val)),(right,yy(val))],HexColor('#E0E3E6'),.4)
        text(29,yy(val)-3,str(val),8)
        text(xx(val)-4,bottom-14,str(val),8)
    line([(left,bottom),(right,bottom)],ink,.6)
    line([(left,bottom),(left,bottom+height)],ink,.6)
    text(17,bottom+height/2,'y',10); text(right+3,bottom-14,'x',10)
    c.saveState()
    clip=c.beginPath(); clip.rect(left,bottom,pw,height); c.clipPath(clip,stroke=0)
    band=list(zip(xx(grid),yy(mean-sd)))+list(zip(xx(grid[::-1]),yy((mean+sd)[::-1])))
    p=c.beginPath();p.moveTo(*band[0])
    for a,b in band[1:]:p.lineTo(a,b)
    p.close(); c.setFillColor(HexColor('#D8E8F2')); c.drawPath(p,fill=1,stroke=0)
    line(list(zip(xx(grid),yy(truth(grid)))),ink,1.4,[4,2])
    line(list(zip(xx(grid),yy(mean))),orange,1.6,[1.5,1.5])
    line(list(zip(xx(grid),yy(pred))),blue,1.1)
    c.setFillColor(ink)
    for a,b in zip(xx(x),yy(y)):c.circle(float(a),float(b),1.6,fill=1,stroke=0)
    c.restoreState()
    if degree==1:
        t=.62; i=np.argmin(abs(grid-t)); a=xx(grid[i]); b=yy(truth(grid[i])); d=yy(mean[i])
        line([(a,b),(a,d)],orange,1.3)
        line([(a-3,b),(a+3,b)],orange,1.3);line([(a-3,d),(a+3,d)],orange,1.3)
        fa(a-6,(b+d)/2,'بایاس',10,orange)
    if degree==11:
        fa(right-8,bottom+height-13,'ناحیه‌ی پهن‌تر: تغییرپذیری بیشتر',10,blue)
    if degree==3:
        j=18; a=xx(x[j]); b=yy(truth(x[j])); d=yy(y[j])
        line([(a,b),(a,d)],ink,.8,[2,1])
        fa(a-6,(b+d)/2+10,'نویز',10)
fa(right,35,'در هر سه نمودار، ۲۵ ورودی و مشاهدات نویزی یکسان‌اند.',10)
items=[(right,20,'تابع واقعی',ink,[4,2]),(right-125,20,'میانگین مدل‌ها',orange,[1.5,1.5]),(right-270,20,'یک مدل برازش‌شده',blue,[])]
for a,b,label,col,dash in items:
    line([(a-18,b+3),(a,b+3)],col,1.3,dash);fa(a-24,b,label,10)
fa(right,5,'ناحیه‌ی سایه‌دار: یک انحراف معیار بالاتر و پایین‌تر از میانگین پیش‌بینی',10)
c.save()
(OUT/'bias-variance-metrics.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
assert metrics['1']['bias_squared']>metrics['3']['bias_squared']
assert metrics['11']['variance']>metrics['3']['variance']
assert metrics['11']['expected_train_mse']<metrics['3']['expected_train_mse']
assert metrics['11']['expected_test_mse']>metrics['3']['expected_test_mse']
print(json.dumps(metrics,indent=2))

tex=r"""\documentclass{article}
\usepackage[paperwidth=480bp,paperheight=610bp,margin=0pt]{geometry}
\usepackage{graphicx,tikz}
\usepackage{xepersian}
\settextfont{XB Yas}
\pagestyle{empty}
\begin{document}
\null
\begin{tikzpicture}[remember picture,overlay,x=1bp,y=1bp]
\begin{scope}[shift={(current page.south west)}]
\node[anchor=south west,inner sep=0pt] at (0,0) {\includegraphics[width=480bp,height=610bp]{bias-variance-base.pdf}};
"""+'\n'.join(labels)+r"""
\end{scope}
\end{tikzpicture}
\end{document}
"""
(OUT/'bias-variance-function.tex').write_text(tex,encoding='utf-8')
exe=shutil.which('xelatex') or str(Path.home()/'AppData/Local/Programs/MiKTeX/miktex/bin/x64/xelatex.exe')
for _ in range(2):
    result=subprocess.run([exe,'-interaction=nonstopmode','-halt-on-error','bias-variance-function.tex'],cwd=OUT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if result.returncode:
        raise RuntimeError(result.stdout.decode('utf-8',errors='replace')[-4000:])
