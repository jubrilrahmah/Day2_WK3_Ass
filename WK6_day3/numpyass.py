import numpy as np
from numpy import arange


print("Assignment")
#Generate an array of numbers between 1 and 100 with both numbers included and find the LCM of the even numbers. 

#creating a 1D array that included to 100
arr1 = np.arange(1,101, 3)
print(arr1)

#using for loop and if to draft out even numbers from the array
arr2= []
for i in arr1:
    if i%2== 0:
        arr2.append(i)

print("\n",arr2)
arr3 = np.array(arr2)
print(arr3)
#solving for lcm using the "lcm function and reduced fuction since numbers are already in an array"
y= np.lcm.reduce(arr3)
print(y)

#second method of usin lambda to filter out even number in the array
nlist = list(filter(lambda x: (x%2 == 0), arr1))
print("\n",nlist)

#returning the list to an array
arr10= np.array(nlist)
print(arr10)
#solving for lcm using the "lcm function and reduced fuction since numbers are already in an array"
lcm = np.lcm.reduce(arr10)
print(lcm)

