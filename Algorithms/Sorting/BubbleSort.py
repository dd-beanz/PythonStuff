def BubbleSort(arr):
    while True:
        corrected = False
        for e in range(len(arr) - 1):
            if arr[e] > arr[e + 1]:
                arr[e], arr[e + 1] = arr[e + 1], arr[e]
                corrected = True
        if not corrected:
            return arr

def BubbleSortDescending(arr):
    while True:
        corrected = False
        for e in range(len(arr) - 1):
            if arr[e] < arr[e + 1]:
                arr[e], arr[e + 1] = arr[e + 1], arr[e]
                corrected = True
        if not corrected:
            return arr
            

print(BubbleSort([2,5,1,8]))  
print(BubbleSortDescending([3,8,23,1,4]))
