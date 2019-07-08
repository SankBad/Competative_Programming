#code
def WaveSort(arr):
	for i in range(0, len(arr)-1, 2):
		arr[i], arr[i+1]= arr[i+1], arr[i]
	return arr
	
T=int(input())
for t in range(T):
    n=int(input())
    arr=input().split()
    WaveArr = WaveSort(arr)
    for i in range(len(WaveArr)):
        print(WaveArr[i], end= ' ')
    print()
