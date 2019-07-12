def NthCatlan(n):
    CatlanArr = [0]*(n+1)
    CatlanArr[0] = 1
    CatlanArr[1] = 1
    i = 2
    while (i<=n):
        for j in range(0, i):
            CatlanArr[i] += CatlanArr[j]*CatlanArr[i-1-j]
        i += 1
    
    return CatlanArr[n] 

NthCatlan(10)
