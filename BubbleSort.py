def BubbleSort(arr):
    length = len(arr)
    for i in range(0, length):
        for j in range(0, length-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
    return arr    
A = [64, 25, 12, 22, 11] 
sortedArr = BubbleSort(A)
sortedArr
