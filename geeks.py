#Find duplicates in O(n) time and O(n) extra space
# Input: n = 7, arr[] = [1, 2, 3, 6, 3, 6, 1]
# Output: 1, 3, 6

def duplicates(arr):
    seen_values = {}
    duplicates = []
    for i,num in enumerate(arr):
        if num in seen_values:
            duplicates.append(num)
        else:
            seen_values[num] = i
            
    return duplicates

array = [1, 2, 3, 6, 3, 6, 1]
# print('The duplicate values are',duplicates(array))

############################################  Question no.2 ######

# Given an array arr[], the task is to find the subarray that has the maximum sum and return its sum.

def maximum_subarray(arr):
    res = arr[0]
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i,len(arr)):
            curr_sum = curr_sum + arr[j]
            if curr_sum > res:
                res = curr_sum
            
    return res

arr = [-2, 6, -3, -10, 0, 2]
# print('The maximum subarray sum is ',maximum_subarray(arr))            


def maximum_prod(arr):
    res = arr[0]
    for i in range(len(arr)):
        curr_prod = 1
        for j in range(i,len(arr)):
            curr_prod = curr_prod * arr[j]
            if curr_prod > res:
                res = curr_prod
    
    return res

# print('The maximum product is ',maximum_prod(arr))

#3 Sum – Find All Triplets with Zero Sum
