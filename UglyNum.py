def UglyNum(n):
    UglyNumArr = [0]*(n+1)
    UglyNumArr[1] = 1
    i = 2
    p, q, r = 0, 0, 0
    x, y, z = 1, 1, 1
    while (i<=n):
        if p==1:
            x +=1
        elif q==1:
            y +=1
        elif r==1:
            z +=1
    
        UglyNumArr[i] = min(2*UglyNumArr[x], 3*UglyNumArr[y], 5*UglyNumArr[z])
        
        if UglyNumArr[i]/UglyNumArr[x]==2:
            p, q, r = 1, 0, 0
        elif UglyNumArr[i]/UglyNumArr[y]==3:
            p, q, r = 0, 1, 0
        elif UglyNumArr[i]/UglyNumArr[z]==5:
            p, q, r = 0, 0, 1
        
        if UglyNumArr[i] == UglyNumArr[i-1]:
            continue
    
        i += 1
    return UglyNumArr[n] 

UglyNum(20)
