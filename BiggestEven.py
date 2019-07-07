def BiggestEven(string):
    even = 0
    for i in string:
        if (int(i)%2==0):
            even = 1
            break
    NumList = []
    for i in string:
        NumList.append(int(i))
    if even==0:
        NumList.sort(reverse=True)
        string1 = ''
        for i in NumList:
            string1 +=str(i)
        return int(string1)
    if even==1:
        MinEven = 11
        for i in NumList:
            if i%2==0:
                if i<MinEven:
                    MinEven = i
        
        NumList.remove(MinEven)
        NumList.sort(reverse=True)
        string1 = ''
        for i in NumList:
            string1 +=str(i)
        string1 += str(MinEven)
        return int(string1)
    
string = '124445434333444304477474449383'
BiggestEvenInt = BiggestEven(string)
BiggestEvenInt
