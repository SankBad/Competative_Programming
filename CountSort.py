def CountSort(arr):
    length = len(arr)
    INPUT = [0 for i in range(256)]
    OUTPUT = [0]*length
    
    for i in arr:
        INPUT[ord(i)]= INPUT[ord(i)]+1
        
    for i in range(256):
        INPUT[i]= INPUT[i]+INPUT[i-1]
    
    for i in range(len(arr)):
        OUTPUT[INPUT[ord(arr[i])] - 1] = arr[i]
        INPUT[ord(arr[i])] -= 1
        
    string = ''
    
    for i in OUTPUT:
        string += i
    
    return string

arr = "geeksforgeeks"
StringOutput = CountSort(arr) 
StringOutput
