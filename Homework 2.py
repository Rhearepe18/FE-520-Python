
# coding: utf-8

# In[171]:


CWID:10438997

#Question 1
#A regular expression is a sequence of characters that define a pattern for searching in a string. 
#For example, the regular expression ’[0−9][a−z]’ corresponds to a two character pattern consisting of 
#a digit (0 to 9) and a lowercase letter (a to z). Write a function that searches for the first occurence 
#of the pattern in a string. Input is a string. Output is None for no match, or the substring for a match.
#Example. myFunction(’abcXYZ01’) returns None. ’abc01XYZ23’ returns ’1X’.


import re
def find_regex(s):     #define funtion
    m = re.search('[0-9][a-z]', s, re.IGNORECASE)      #assign search 
    if m:
        print(m.group())
    else:
        print("None")
    
find_regex('abcXYZ01')


# In[172]:


find_regex('abc01XYZ23')


# In[180]:


#Question 2
#Write a function that applies a function to an iterator. 
#Input is a function and an iterator.
#Output is the iterator obtained by applying the function to each entry.
#Example. myFunction(lambda x: 2∗x, range(3)) returns an iterator such that 
#list(myFunction(lambda x: 2∗x, range(3))) returns [0,2,4].

import pprint      
import math
list1=[]
def xyz(kk,T):
    for i in range (0,T):
        list1.append((kk*i))
    pprint.pprint(list1)
    
# the function xyz creates a list of length T where each list element is multiplied by the variable kk.
# the input to the function in my example is int(4) and int(mat.pow(5,1))which is an iterator and a function. 
#The output is an iterator obtained 
# by applying the function to each entry. math.pow(5,1) returns a value equal to 5^1.










# In[174]:


xyz(int(4), int(math.pow(5,1)))


# In[181]:



#Question 3
# An enumerated type (or an enum for short) is a data type relating strings to integers. 
#Think of an enum as a dictionary with strings for keys and integers for values e.g. {’Left’:1,’Right’:2 }. 
#Create a class Enum such that
#• The constructor takes a list of strings
#• The attributes are the strings with values 0,1,2, etc.

#• The class has a method called cast that inputs an integer 0,1,2, etc. and outputs the corresponding string.
#Example. Set temp = Enum([’Left’,’Right’]). We have print(temp.Left) re- turns 0. We have temp.cast(1) returns ’Right’.
#Hint. Save a copy of the list passed to the constructor. Use setattr to set the at- tributes.


class Enum:
    def __init__(construct, ls): 
        ls_temp=[]
        construct.ls_temp = ls
        for i in range(len(ls)):
            #print(ls[i])
            attr = ls[i]
            setattr(construct, attr, i)
            
    def cast(construct, i):
        for k in construct.ls_temp:
            if getattr(construct, k) == i:
                return(k)
        
 
        
input_ls  = ['Left', 'Right', 'Nowhere']
x = Enum(input_ls)
print(x.Right)

x.cast(0)


# In[182]:



#Question 4

#The singleton pattern is a design pattern in object oriented programming where only a single instance of the class
#can be constructed. Consider a class Inner with no methods and one integer attribute called intAttribute. 
#Devise a class Outer that contains
#• thedefinitionoftheclassInnerincludingtheconstructorwhereself.intAttribute gets set
#• static attribute instanceInner set initially to None
#• constructor that sets instanceInner to Inner if instanceInner is None
#Example. First set temp1 = Outer(1). Second set temp2 = Outer(2). 
#We have print(temp2.instanceInner.intAttribute) returns 1

class Outer:
    class Inner:
        def __init__(self, arg):
            self.intAttribute = arg
    instanceInner = None
    def __init__(self, arg):
        if not Outer.instanceInner:
            Outer.instanceInner = Outer.Inner(arg)


# In[183]:


temp1 = Outer(1)
temp2 = Outer(2)
print(temp2.instanceInner.intAttribute)


# In[218]:


#Bonus Question 1

#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".

def findPrefix(self, str1, str2):
        min_len = min(len(str1), len(str2))   
       
        for i in range(0, min_len):
            if str1[i] != str2[i]:
                return str1[0:i]
        return str1[0:min_len]


# In[219]:


findPrefix('flight','flight','flow')


# In[220]:


findPrefix("dog","racecar","car")


# In[185]:


#Bonus question 2
#Merge two sorted linked lists and return it as a new list. 
#The new list should be made by splicing together the nodes of the first two lists.

def merge(aList, bList):
    newList = []
    while (aList or bList): # single empty list won't stop the loop
        if not bList or (aList and aList[0] < bList[0]):
            # either bList is empty, or aList has next item
            newList.append(aList.pop(0))
        else:
            # bList has next item
            newList.append(bList.pop(0))
    
    
    return newList

list1 = [3, 4, 8, 9]
list2 = [1, 2, 5, 8]

print(merge(list1, list2))

