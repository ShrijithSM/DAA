'''
l = []

nums = int(input("Enter the number of elements: "))
for i in range(nums):
    l.append(int(input("Enter the element: ")))

target = int(input("Enter the target element: "))


print(binarySearch(l,target,0,len(l)-1))
'''

def binarysearch(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = int((low+high)//2)

        if array[mid] == target:
            return mid
        
        elif array[mid] < target:
            low = mid+1
        
        else:
            high= mid-1
    return -1


print(binarysearch([10,20,30,40,50],20))