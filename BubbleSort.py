def swap(a,b):
    temp = a
    a = b
    b = temp 
    return (a , b)

def BubbleSort(arr):
    
    for i in range(len(arr)):
        for e in range(0,len(arr) - 1):
            a = arr[e]
            b = arr[e+1]
            if a < b:
                #(a,b) = swap(a,b)
                arr[e] = a
                arr[e+1] = b
            elif a > b:
                (b,a) = swap(a,b)
                arr[e] = b
                arr[e+1] = a 
    return arr

def ReverseBubble(arr):
    for i in range(len(arr)):
        for e in range(0,len(arr) - 1):
            a = arr[e]
            b = arr[e+1]
            if a > b:
                #(a,b) = swap(a,b)
                arr[e] = a
                arr[e+1] = b
            elif a < b:
                (b,a) = swap(a,b)
                arr[e] = b
                arr[e+1] = a 
    return arr