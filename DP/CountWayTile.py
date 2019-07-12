def CountWayTile(W):
    
    CountArr = [0]*(W+1)
    CountArr[1] = 1
    CountArr[0]= 1
    i = 2
    while(W>=i):
        CountArr[i] = CountArr[i-1] + CountArr[i-2]
        i += 1
    return CountArr[W]
    
t=int(input())
for i in range(t):
    a=int(input())
    print(CountWayTile(a))
