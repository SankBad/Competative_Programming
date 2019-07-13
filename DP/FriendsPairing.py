def FriendsPairing(n):
    FreindsPairArr = [0]*(n+1)
    FreindsPairArr[1] = 1
    FreindsPairArr[2] = 2
    i = 3
    while (i<=n):
        FreindsPairArr[i] = FreindsPairArr[i-1] + (i-1)*FreindsPairArr[i-2]
        i += 1
        
    return FreindsPairArr[n]%(10**9+7)
    
t=int(input())
for i in range(t):
    a=int(input())
    print(FriendsPairing(a))
