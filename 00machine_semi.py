import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt


def min_sq(x,y):
	x_bar,y_bar=np.mean(x),np.mean(y)
	beta_1=np.dot(x-x_bar,y-y_bar)/np.linalg.norm(x-x_bar)**2
	beta_0=y_bar-beta_1*x_bar
	return [beta_1,beta_0]

#何のために何の値を出力したいかを意識して予習する
#目的と最終的に出しやすい値を意識する

N=100
a=np.random.normal(loc=2,scale=1,size=N)
b=randn(1)
x=randn(N)
y=a*x+b+randn(N)
a1,b1=min_sq(x,y)
xx=x-np.mean(x);yy=y-np.mean(y)#中心化
a2,b2=min_sq(xx,yy)

x_seq=np.arange(-5,5,0.1)
y_pre=x_seq*a1+b1
yy_pre=x_seq*a2+b2
plt.scatter(x,y,c="black")
plt.axhline(y=0,c='black',linewidth=0.5)
plt.axvline(x=0,c="black",linewidth=0.5)
plt.plot(x_seq,y_pre,c="blue",label="中心化前")
plt.plot(x_seq,yy_pre,c="orange",label="中心化後")
plt.legend(loc="upper left")
plt.show()

