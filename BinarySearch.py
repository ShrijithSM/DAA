# Binary Search in python


def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if x == array[mid]:
            return mid

        elif x > array[mid]:
            low = mid + 1

        else:
            high = mid - 1

    return -1

'''
l = []

nums = int(input("Enter the number of elements: "))
for i in range(nums):
    l.append(int(input("Enter the element: ")))

target = int(input("Enter the target element: "))


print(binarySearch(l,target,0,len(l)-1))
'''