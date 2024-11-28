def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  
'''
l = []

nums = int(input("Enter the number of elements: "))
for i in range(nums):
    l.append(int(input("Enter the element: ")))

target = int(input("Enter the target element: "))

print(linear_search(l, target))
'''