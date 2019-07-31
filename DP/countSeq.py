# https://www.geeksforgeeks.org/count-even-length-binary-sequences-with-same-sum-of-first-and-second-half-bits/

def countSeq(n):
    countSeqArr = [-1]*(n+1)
    countSeqArr[0] = 1
    i = 1
    SUM = 1
    while (i<n+1):
        countSeqArr[i] = ((n-i+1)*countSeqArr[i-1])/i
        SUM += countSeqArr[i]* countSeqArr[i]
        i += 1
    return int(SUM)

print(countSeq(2))
