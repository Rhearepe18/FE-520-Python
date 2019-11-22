
# coding: utf-8
Homeowrk 4
ID: 10438997
# In[60]:


import numpy as np
import matplotlib.pyplot as plt


# In[61]:


M = 10000 #number of samples
temp = np.random.randn(10000)


# In[62]:


r = 0.05
sigma = 0.2
T = 3
K = 105
S0 = 100 #value of S(0)


# In[63]:


np.exp(temp)
temporary = np.exp((r - 0.5 * sigma**2) * T + np.sqrt(T) * sigma * temp)


# In[64]:


#Write a function callOption with inputs

def callOption(S0, K, T, sigma, r, M):
    random_numbers = np.random.randn(M)
    
    temp = np.empty(M)
    temporary_sum = 0
    counter = 0 
    
    for Nj in random_numbers:
        exponential_exp = S0 * np.exp((r - 0.5 * sigma**2) * T + np.sqrt(T) * sigma * Nj)
        maximum = max(exponential_exp - K, 0)
        temporary_sum = temporary_sum + maximum
        temp[counter] = exponential_exp
        counter = counter + 1
    
    averaged = temporary_sum/M
    
    return np.exp(-r * T) * averaged, temp


# In[65]:


#Evaluate callOption
value, samples = callOption(S0, K, T, sigma, r, M)


# In[66]:


# Create a histogram
plt.hist(samples, bins = 400)
plt.show()


# In[67]:


#Question 2


# In[68]:


import math


# In[127]:


P = 100
PV = 90
T = 1
f = 4
c = 0.05


# In[128]:


#(a) Write a function bondValue
def bondValue(P, T, f, c, y):
    summation = 0.0
    for j in range(1, (f * T) + 1):
        summation = summation + (c/f) * P * math.exp(-y*(j/f))
    
    PV = math.exp(-y * T) * P + summation
    return(PV)
    
    


# In[129]:


x = bondValue(P,T,f,c,0.03)  #yeild is 3%


# In[130]:


x


# In[131]:


#(b) Write a function bondDuration 
def bondDuration(P, T, f, c, y):
    summation2 = 0.0 
    for j in range(1, (f * T) + 1):
        summation2 = summation2 + (c/f)*P*(j/f)*math.exp(-y*(j/f))
        
    numerator = math.exp(-y*T)*P*T + summation2
    denominator = math.pow(x,-1)
    return(numerator*denominator)
         
         


# In[132]:


z = bondDuration(P,T,f,c,0.03)


# In[133]:


z


# In[137]:


import scipy
from scipy import optimize


# In[138]:


#Define a function bondYield with input y
P = 100
PV = 90
T = 1
f = 4
c = 0.05


# In[139]:


def bondYield(y):
    return bondValue(P, T, f, c, y) - PV


# In[140]:


scipy.optimize.newton(bondYield, 0.03)


# In[166]:


#Write a function Kendall
import numpy as np
def Kendall(X,Y):
    
    n=len(X)
    i=0
    j=0
    c=0
    d=0
    tx=0
    ty=0
    tau=np.empty(shape=(10,10))
    for i in range(0,n):
        for j in range(0,n):
            if(np.sign(X[i]-X[j])*np.sign(Y[i]-Y[j]))>0:
                c=c+1
               
            if(np.sign(X[i]-X[j])*np.sign(Y[i]-Y[j]))<0:
                d=d+1
                
            if(np.sign(X[i]-X[j])==0 and np.sign(Y[i]-Y[j])!=0):
                tx=tx+1
                
            if(np.sign(X[i]-X[j])!=0 and np.sign(Y[i]-Y[j])==0):
                ty=ty+1
                
    denomenator = math.sqrt(c+d+tx)*math.sqrt(c+d+ty)
    return (c-d)/denomenator
   
    
            
A = np.random.randn(10)
B = np.random.randn(10)
Kendall(A,B)
        
    
    


# In[142]:


import pandas as pd


# In[143]:


temp  = pd.DataFrame(np.random.randn(10,10), index = range(10))


# In[144]:


temp.corr(method = 'kendall')  


# In[145]:


import os
import pandas as pd
print (os.getcwd())


# In[146]:


aapl = pd.read_csv('AAPL.csv')


# In[112]:


aapl


# In[147]:


import sqlite3


# In[148]:


conn = sqlite3.connect("MSFT.db")


# In[149]:


cur = conn.cursor()


# In[150]:


cur.execute('SELECT * FROM MSFT')


# In[91]:


cur.fetchall()


# In[117]:


msft = pd.read_sql('SELECT * FROM MSFT', conn)


# In[118]:


msft


# In[169]:


aapl['Close'].corr(msft['Close'], method = 'kendall') #kendall statistic


# In[121]:


aapl['Close'].corr(msft['Close']) #correlation


# In[170]:


Kendall(aapl['Close'],msft['Close'])

