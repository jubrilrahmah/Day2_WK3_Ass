import numpy
from numpy import arange

print("Assignment")
#Create a list of integers between 5.5 and 20.5. Write a python program using the lambda function that does the following;
#count  the even and odd  numbers in the list .
#Square and cube every number in the list.



mylist = [*arange(5.5, 20.5, 1.5)]
print ("List of numbers in range 5.5 to 20.5 with a step of 1.5")
print(mylist)

#creating the odd and even list using the filter fuction
even_list = list(filter(lambda x: (x%2 == 0), mylist))
print("\nThe even numbers are: ")
print(even_list)
print("the number of even number in the list is: ", len(even_list))

print("\nThe even numbers are: ")
odd_list = list(filter(lambda x: (x%2 != 0), mylist))
print(odd_list)
print("the number of even number in the list is: ", len(odd_list))

#doubling and cubin the numbers in the list using the cube function
print("\n The square of the numbers in the original list")
d_list = list(map(lambda x: x ** 2 , mylist))
print(d_list)

print("\n The cube of the numbers in the original list")
c_list = list(map(lambda x: x ** 3 , mylist))
print(c_list )
