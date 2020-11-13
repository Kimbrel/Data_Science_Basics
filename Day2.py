# DAY 2

#Questions 1:

list = []
print('Enter 10 numbers')

for x in range(10):
    x = int(input())
    if (x % 2 == 0):
        list.append(x)
print(list)
#------------------------------------------------------------------

#Question 2

numbers = [1, 2, 3, 4, 5]
cube = [number**3 for number in numbers if number > 2]
print(cube)
#-------------------------------------------------------------------------

# Question 3

n = int(input())
d = {}

for i in range(n):
    keys = i+1
    values = keys * keys 
    d[keys] = values
print(d)

#---------------------------------------------------------------------  
# Question 4

import math

direction = []
value = []
n = int(input())
for i in range(n):
   a, b = input().split(" ")
   direction.append(a)
   value.append(int(b))

x = int(value[0]-value[1])
y = int(value[2] - value[3])
position = math.sqrt(x**2 + y**2)
print(round(position))

#----------------------------------------------------------------------

