def SelectionSort(arr):
    length = len(arr)
    SortedArr = [0]*length
    for j in range(0, length):
        min = arr[j]
        for i in range(j, length):
            if min>arr[i]:
                min=arr[i]
                x=i
        arr[j], arr[x]=arr[x], arr[j]
        SortedArr[j]=min
    
    for j in range(0, length):
        print(SortedArr[j], end=" ")
    # add code here
    
A = [64, 25, 12, 22, 11] 
SelectionSort(A)
