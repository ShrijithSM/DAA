"""
function mergeSort(array)
    if length of array <= 1
        return array
    middle = length of array / 2
    leftArray = mergeSort(first half of array)
    rightArray = mergeSort(second half of array)
    return merge(leftArray, rightArray)

function MERGE(A, left, middle, right)
    // // Merge the subarrays A[left..middle] and A[middle+1..right] into a single sorted subarray.
"""

# def mergeSort(Array):
#     if len(Array) <= 1:
#         return Array
#     middle = len(Array)//2
#     left = mergeSort()

def mergeSort(A, left, right):
    if left<right:
        middle = (left+right)/2
        mergeSort(A,left,middle)
        mergeSort(A,middle+1,right)
        merge(A, left, middle)

def merge(A, left, middle, right):
    A = 

