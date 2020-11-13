# DAY 3

# Question 1
import numpy as np

a = np.arange(2,50,3)

#------------------------------------------------------------------
#Question 2

import numpy as np

lst1 = []
lst2 = []

lst1 = input("Enter 1st list of 5 elements separated by space ").split(" ")
lst2 = input("Enter 2nd list of 5 elements separated by space ").split(" ")
lst1 = np.array(lst1)
lst2 = np.array(lst2)
lst3 = np.concatenate((lst1, lst2), axis=0)
print(lst3)
lst1 = np.sort(np.array(lst1))
lst2 = np.sort(np.array(lst2))
print(lst1)
print(lst2)

#----------------------------------------------------------------------
#Question 3

import numpy as np

arr = np.arange(12)
print(arr.ndim, arr.size)

#-----------------------------------------------------------------------
# Question 4

import numpy as np

arr = np.arange(12)
print(arr.shape)
arr=arr[np.newaxis,:]
print(arr.shape)

#---------------------------------------------------------------------------
# Question 5
import numpy as np

A = np.identity(3)
B = np.identity(3)

a= np.vstack((A,B))
b= np.hstack((A,B))
#---------------------------------------------------------------------------

#Question 6


input_list = [1, 2, 2, 5, 8, 4, 4, 8] 
 
l1 = [] 
  

count = 0

for item in input_list: 
    if item not in l1: 
        count += 1
        l1.append(item) 

print("No of unique items are:", count)
print("Unique items are:", l1)
