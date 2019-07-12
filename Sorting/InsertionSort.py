def InsertionSort(a):
    length= len(a)
    for i in range(1, length):
        num = a[i]
        j = i-1
        while (num<a[j] and j>=0):
            temp=a[j]
            a[j]=num            
            a[j+1]=temp
            j =  j-1

arr = [12, 11, 13, 5, 6] 
InsertionSort(arr) 
arr
