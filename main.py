from InsertionSort import insertionSort
from LinearSearch import linear_search
from BinarySearch import binarysearch
from QuickSort import quickSort

def arr():
    l = []
    nums = int(input("Enter the number of elements: "))
    for i in range(nums):
        l.append(int(input("Enter the element: ")))
    return l


print("Main Menu\n1. Binary Search\n2. Linear Search\n3. Insertion Sort\n4. Quick Sort")
fn = int(input("Enter your option: "))

if fn == 1:
    l = arr()
    target = int(input("Enter the target element: "))
    print(f"Binary Search Result: {binarysearch(l,target)}")

elif fn==2:
    l = arr()
    target = int(input("Enter the target element: "))
    print(f"Linear Search Result: {linear_search(l, target)}")

elif fn == 3:
    l = arr()
    insertionSort(l)
    print("Array after Insertion Sort: ")
    for i in range(len(l)):
        print(l[i],end = " ")

elif fn == 4:
    l = arr()
    n = len(l)
    quickSort(l, 0, n - 1)
    print("Array after Quick Sort: ")
    for val in l:
        print(val, end=" ") 
        