#Reverse an array
arr = [1,2,3,4,5]
arr.reverse()
print(arr)

#using index
print(arr[::-1])

#using for loop
reversed_arr = []
for i in range(len(arr)-1,-1,-1):
    reversed_arr.append(arr[i])

print(reversed_arr)

#Find the maximum and minimum element in an array

import random
min = arr[random.randint(0,len(arr))]
max = arr[random.randint(0,len(arr))]
for i in range(len(arr)):
    if arr[i] < min:
        min = arr[i]
    if arr[i] > max:
        max = arr[i]
        
print('The minimun number is ',min)
print('The maximum number is ',max)

#Check if a string is a palindrome
def ispalindrome(s):
    reversed_s = s[::-1]
    if reversed_s == s:
        print('palindrome')
    else:
        print('Not palindrome')
    
ispalindrome('raceca')

#Left rotate an array by two position
arr = [1,2,4,5,6]
for i in range(2):
    popped_value = arr.pop(0)
    arr.append(popped_value)

print('Array after two rotation',arr)

#Move all zeros to the end of the array
arr = [1,0,2,3,0,45,0]
for i in range(len(arr)):
    if arr[i] == 0:
        arr.pop(i)
        arr.append(0)
    
print('Array after adding zeros to the end',arr)

