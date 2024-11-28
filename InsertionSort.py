def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


'''
arr = [112,43,23,2421,42222221,242242,3243221,123312,312314,41322,321,3242534523,35342,4,2353333,32,43525,2353,2332,522,32,22]

insertionSort(arr)
# printArray(arr)

for i in range(len(arr)):
    print(arr[i],end = " ")
'''