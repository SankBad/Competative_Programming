#https://www.geeksforgeeks.org/the-stock-span-problem/
def calculateSpan(price, n, S):
    S[0] = 1
    for i in range(1, n):
        p = 1
        while(price[i]>price[i-p]):
            p += 1
            if i-p==-1:
                break
        S[i] = p
    return S
            


price = [10, 4, 5, 90, 120, 80] 
n = len(price) 
S = [None] * n 
  
# Fill the span values in list S[] 
calculateSpan(price, n, S)
S
