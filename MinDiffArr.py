#chocolate-distribution-problem
#https://www.geeksforgeeks.org/chocolate-distribution-problem/
import sys

def MinDiffArr(arr, m):
    MinDiff = sys.maxsize
    arr.sort()
    for i in range(0, len(arr)-m+1):
        diffVal= arr[i+m-1]-arr[i]
        if diffVal<MinDiff:
            MinDiff = diffVal
    return MinDiff
    


if __name__ == "__main__": 
    arr = [12, 4, 7, 9, 2, 23, 25, 41, 
          30, 40, 28, 42, 30, 44, 48,  
          43, 50]
    m = 7 # Number of students 
    MinDiff = MinDiffArr(arr,m)
    print(MinDiff)
