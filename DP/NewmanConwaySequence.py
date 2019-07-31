def NewmanConwaySequence(n):
    NewmanConwaySequenceArr = [-1]*(n+1)
    NewmanConwaySequenceArr[1] = 1
    NewmanConwaySequenceArr[2] = 1
    i = 3
    while(n!=i-1):
        NewmanConwaySequenceArr[i] =  NewmanConwaySequenceArr[NewmanConwaySequenceArr[i-1]] + NewmanConwaySequenceArr[i-NewmanConwaySequenceArr[i-1]]
        i += 1
    return NewmanConwaySequenceArr[n]

print(NewmanConwaySequence(10))
