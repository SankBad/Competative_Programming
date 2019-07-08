#https://practice.geeksforgeeks.org/problems/left-out-candies/0

def LeftOutCandies(N, M):
    i = 1
    while(M-i>=0):
        M = M - i
        i = i+1
        if i == N+1:
            i = 1
    return print(M)

t=int(input())
for i in range(t):
     N, M = list(map(int,input().split()))
     LeftOutCandies(N, M)
