def BinarySearch(L, start, end, K):
    if end>=start:
        n = start + int((end-start)/2)
        if L[n]==K:
            return n+1
        elif L[n]<K:
            return BinarySearch(L, n+1, end, K)
        elif L[n]>K:
            return BinarySearch(L, start, n-1, K)
    else:
        return -1
    
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = BinarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
