
# coding: utf-8

# In[1]:


#Question 1

import numpy as np
from itertools import islice
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
def buckets(listInput, intBuckets):
    

    
    list_min = min(listInput)
    list_max = max(listInput)
    s = list_max - list_min
    interval = int(s/intBuckets)
    a = [c for c in range(list_min, list_max+1)]
    b = []
    c = []
    listInput.sort()
    
    
    l = [a[i:i+interval] for i in range(0, len(a),interval)]
    
    
    for j in range (0,intBuckets):
        b.append(l[j][0])
        
    b.append(list_max)
    
    plt.hist(listInput, b, facecolor='blue', rwidth=0.7)
    plt.show()

    
  

    print(listInput)
   


    
 


# In[2]:


listInput = np.random.randint(-100, 100, 100)
buckets(listInput, 7)


# In[3]:


#Question 2

import matplotlib.pyplot as plt
import numpy as np
class abstractRandom(object):
    def __init__(self, seed):
        self.current = seed
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == len(self.current):
            raise StopIteration

        self.current_updated = self.generator(self.current[self.index])
        self.index = self.index + 1
        return self.current_updated
        
class Random(abstractRandom):
    def __init__(self, seed, generator):
        self.current = seed
        self.generator = generator
        x = super().__init__(self.current)
        return (x)


# In[4]:


m = 771
a = 331
b = 17
input_generator = lambda x: ((a*int(m*x) + b) % m)/m 
#ls = np.arange(0, 1, 0.01)
ls = np.random.random_sample(100)
transformation_function = lambda x: round(x)

random_numbers = []
transformed_numbers = []
y = Random(ls, input_generator)
for i in y:
    random_numbers.append(i)
    if transformation_function(i) == 0:
        transformed_numbers.append(-1)
    else:
        transformed_numbers.append(1)


# In[5]:


xaxis = np.arange(0,100,1)
yaxis = np.cumsum(transformed_numbers)
plt.plot(xaxis, yaxis, 'k-*')
plt.show()


# In[6]:


#Question 3

import types
import math
import numpy as  np
import matplotlib.pyplot as plt

def predictorCorrector(T, N, y0, f):
    h = T/N
    aryOutput = np.zeros(N+1)
    t = np.zeros(N+1)
    
        
    aryOutput[0] = y0
    for n in range(1,N+1):
        t[n] = n * h
        aryOutput[n] = aryOutput[n-1] + 0.5*h*(f(t[n-1],aryOutput[n-1]) + f((t[n-1] + h),  (aryOutput[n-1] + h*f(t[n-1],aryOutput[n-1]))))
        # aryOutput[n] = aryOutput[n-1] + 0.5*(h*f(t[n-1],aryOutput[n-1]) + f((t[n-1] + h), (aryOutput[n-1] + h*f(t[n-1],aryOutput[n-1]))))
        
    
    return aryOutput

f = lambda t,aryOutput: aryOutput
T = 2**4
N = 2**10
y0 = 1
a = np.zeros(N + 1)
a = predictorCorrector(T,N,y0,f)
print(a)


plt.plot(np.linspace(0,T,N+1), np.exp(np.linspace(0,T,N+1)),'k*', label='exponential')

plt.plot(np.linspace(0,T,N+1), predictorCorrector(T,N,y0,f),'r', label='approximation to exponential')
plt.plot(np.linspace(0,T,N+1), a,'r', label='approximation to exponential')
plt.legend()
plt.show()

