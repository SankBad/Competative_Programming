def MergeSort(arr):
    length = len(arr)
    if(length > 1):
        n = int(length/2)
        LeftArr = arr[0:n]
        RightArr = arr[n:length]
        MergeSort(LeftArr)
        MergeSort(RightArr)
        
        i = j = k = 0
        
        while (i < len(LeftArr) and j < len(RightArr)):
            if LeftArr[i]< RightArr[j]:
                arr[k] = LeftArr[i]
                i = i + 1
            else:
                arr[k] = RightArr[j]
                j = j+1
            k = k+1
        # Checking if any element was left 
        while i < len(LeftArr): 
            arr[k] = LeftArr[i] 
            i+=1
            k+=1
          
        while j < len(RightArr): 
            arr[k] = RightArr[j] 
            j+=1
            k+=1
    return arr
    
    

arr = [12, 11, 36, 13, 25, 5, 6] 
SortedArr1 = MergeSort(arr) 
SortedArr1
