def LinearSearch(L, K):
    length = len(L)
    for i in range(length):
        if L[i]==K:
            return i+1
    return -1
  
# Driver Code 
arr = [ 2, 3, 4, 10, 40 ]; 
x = 10; 
n = len(arr); 
result = LinearSearch(arr, x) 
if(result == -1): 
    print("Element is not present in array") 
else: 
    print("Element is present at index", result);
