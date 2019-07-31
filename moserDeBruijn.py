def moserDeBruijn(n):
    moserDeBruijnArr = [-1]*(n+1)
    moserDeBruijnArr[0] = 0
    moserDeBruijnArr[1] = 1
    i = 2
    while(n!=i):
        if i%2==0:
            moserDeBruijnArr[i] = 4*moserDeBruijnArr[int(i/2)]
        else:
            moserDeBruijnArr[i] = moserDeBruijnArr[i-1]+1
        i += 1
    return moserDeBruijnArr[n-1]    
    
    

n = 15
print(moserDeBruijn(15))
