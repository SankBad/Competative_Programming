def BinomialCoeff(n, k, CoeffArr):
    if n==k:
        return 1
    if k==0:
        return 1
    if CoeffArr[n][k] == -1:
        CoeffArr[n][k] = BinomialCoeff(n-1, k-1, CoeffArr) + BinomialCoeff(n-1, k, CoeffArr)
    return CoeffArr[n][k]

def BinomialCoeffCal(n, k):
    CoeffArr = [[-1 for x in range(k+1)] for x in range(n+1)] 
    return BinomialCoeff(n, k, CoeffArr)

    

BinomialCoeffCal(4,2)   
