

#Question 1

#write a function to remove duplicate entries in a list of integers. 

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      

duplicate = [2, 4, 10, 20, 5, 2, 20, 4,4,5,3,2,3,2,2,6,7,5,7,33,12,43] 
print(Remove(duplicate)) 

duplicate = [2,2,2,3,3,3,3,3,3,2,2,3,2,1,4,1,4,1,6,5,6,5]
print(Remove(duplicate))

#Question 2

#Write a function to produce the subsets of a list of integers containing two elements. 
#Input is a tuple of integers. Output is a tuples of tuples, each containing two elements.

import itertools
def subset(arg):
   
    
    sets = []
    for i in range(0, len(arg)):
        listing = [list(x) for x in itertools.combinations(arg, i)]
        sets.extend(listing)
    return sets

subset([1, 2, 3])

#Question 3
#Write a function to remove white space from strings. Input is a string.
#Output is the string with any whitespace removed.
#Example. myFunction(‘‘ text with spaces ’’) returns ‘‘textwithspaces’’
def removeSpaces(string):
    string = string.replace(' ','')
    return string
 
string = "text with spaces  "
print(removeSpaces(string))


string = "   The stock market crashed    "
print(removeSpaces(string))


#Question 4
#Write a function to add or update the value of dictionary. 
#The input is a dictionary, key and value. 
#The output is the same dictionary with either a new key and valuing or an updated value to an existing key.


#Set myDictionary = {’a’:1,’b’:2}. Calling myFunction(myDictionary,’a’,4) 
#would update the ’a’ entry in myDictionary to yield {’a’:4,’b’:2} .
#Now calling myFunction(myDictionary,’c’,10) would change myDictionary to be {’a’:4,’b’:2,’c’:10}.

mydictionary = {'a':1, 'b':2}
def dict(dictionary,key,value):
    if key in dictionary:
        dictionary[key] = value
       
    elif key not in dictionary:
        dictionary[key] = value
       
    else:
        dictionary[key] = [dictionary[key], value]


dict(mydictionary,'a',5)
mydictionary

dict(mydictionary,'c',10)
mydictionary


dict(mydictionary,'a',20)
mydictionary

#Bonus questions


#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example:

#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].


def twoSum(nums, target):
        ls = []
        for i in range(0, len(nums)):
            item = target - nums[i]
            nums[i] = "done"
            if item in nums:
                ls.append(i)
                ls.append(nums.index(item))
                return ls



nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))



nums = [2, 7, 11, 15, 30]
target = 18
print(twoSum(nums, target))

#Given a 32-bit signed integer, reverse digits of an integer.

#Example 1:

#Input: 123
#Output: 321
#Example 2:

#Input: -123
#Output: -321
import sys
def reverse(x):
    if x <sys.maxsize-1  or x > -sys.minsize:

            if str(x)[0] == '-':
                number = list(str(x))
                number.pop(0)
                number.append('-')
                number.reverse()
                rev_num = ''.join(number[:])
                return int(rev_num)
            else:
                return int(str(x)[::-1])
    else:
            return 0





reverse(432)


reverse(234)


reverse(-3425)

