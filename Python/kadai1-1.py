#!/usr/bin/python

import math
import numpy as np
class Fc:
  def __init__(self, n_in, n_out, relu=True, seed=0):
    self.n_in=n_in
    self.n_out=n_out
    self.relu=relu
    np.random.seed(seed) 
    if relu:
      self.w=np.random.normal(0, math.sqrt(2.0/n_in), (n_out, n_in))
      self.relu0=None
    else:
      self.w=np.random.normal(0, math.sqrt(1.0/n_in), (n_out, n_in))
    self.b=np.zeros((n_out,1))
    self.x=np.zeros((n_in,1))
    self.dEdx=np.zeros((n_in,1))
    self.dEdw=np.zeros((n_out,n_in))
    self.dEdb=np.zeros((n_out,1))
    self.count=0
    self.mdw=np.zeros((n_out,n_in))
    self.mdb=np.zeros((n_out,1))


  def __call__(self,x): 
    self.x = x
    self.y = np.dot(self.w, x) + self.b
    if self.relu:
        self.relu0= self.y<=0
        self.y[self.relu0]=0
    return self.y

  def backward(self, dEdy):
    if self.relu:
        dEdy[self.relu0]=0
    dydx = np.transpose(self.w)
    dydw = np.transpose(self.x)

    self.dEdx = np.dot(dydx, dEdy)
    self.dEdw += np.dot(dEdy, dydw)
    self.dEdb += dEdy
    self.count +=1
    return self.dEdx

  def clear_grad(self):
      self.dEdw=0
      self.dEdb=0
      self.count=0

  def update(self, lr=0.001):
      self.w -= self.dEdw/self.count * lr
      self.b -= self.dEdb/self.count * lr
      self.clear_grad()
    
  def updatem(self, lr=0.001, mu=0.9):
      #self.mdw = {yourself}
      #self.mdb = {yourself} 
      self.w += self.mdw
      self.b += self.mdb
      self.clear_grad()
      
fc1=Fc(1,20)
fc2=Fc(20,20)
fc3=Fc(20,1,False)

def f(x):
    return 0.5*(x-2)**2-5

X_train=np.arange(-10,10,0.01,dtype=np.float32)
Y_train= f(X_train)
X_train=np.reshape(X_train,[-1,1])   # (2000,)  -> (2000,1)
Y_train=np.reshape(Y_train,[-1,1]) 
num_train=np.size(X_train)

X_val=np.arange(-8,8,0.1,dtype=np.float32)
Y_val= f(X_val)
X_val=np.reshape(X_val,[-1,1])
Y_val=np.reshape(Y_val,[-1,1])
num_val=np.size(X_val)

#%matplotlib inline
import matplotlib.pyplot as plt
from IPython import display

x0=np.reshape(X_val,[-1])

lr=0.001
num_epoch=150
num_batch=100
losses=np.array([])
losses_val=np.array([])
ep=np.array([])
fig=plt.figure()
fig1 = fig.add_subplot(121)
fig2 = fig.add_subplot(122)
for epoch in range(num_epoch):
    shuffler = np.random.permutation(num_train)
    X_train=X_train[shuffler]
    Y_train=Y_train[shuffler]
    for n in range(0, num_train, num_batch):
        loss=0
        for i in range(num_batch):

          y=fc3(fc2(fc1(np.c_[X_train[n+i]])))

          dEdx=y-np.c_[Y_train[n+i]]
          loss+=(dEdx**2)*0.5

          dEdx=fc3.backward(dEdx)
          dEdx=fc2.backward(dEdx)
          dEdx=fc1.backward(dEdx)

        fc1.update(lr)
        fc2.update(lr)
        fc3.update(lr)

        if n==0:

          losses=np.append(losses,loss/num_batch)
          ep=np.append(ep,epoch)

          loss_val=0
          Y_pred=np.array([])
          for i in range(num_val):

            y=fc3(fc2(fc1(np.c_[X_val[i]])))
            Y_pred=np.append(Y_pred,y)

            dEdx=y-np.c_[Y_val[i]]
            loss_val+=(dEdx**2)*0.5    

          losses_val=np.append(losses_val, loss_val/num_val)
        
          display.clear_output(wait = True)
          fig1.axis([0, num_epoch, 0, 50])
          fig1.plot(ep,losses,"b")
          fig1.plot(ep,losses_val,"r")
          fig2.axis([-8,8,-10,30])
          y0=np.reshape(Y_pred,[-1])
          fig2.plot(x0,y0,"b")
          fig2.plot(x0,f(x0),"r")
          display.display(fig)
          if epoch<num_epoch-1:
            fig2.cla()
display.clear_output(wait = True)
print "loss_val:",loss_val
