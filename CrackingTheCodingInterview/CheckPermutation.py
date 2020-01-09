def CheckPermutation(string1, string2):
    Dict1 = {}
    Dict2 = {}
    for i in string1:
        if i in Dict1:
            Dict1[i] = Dict1[i] + 1
        else:
            Dict1[i] = 1
    for j in string2:
        if j in Dict2:
            Dict2[j] = Dict2[j] + 1
        else:
            Dict2[j] = 1
    if Dict1 == Dict2:
        return True
    else:
        return False

string1 = 'abcdef'
string2 = 'cbafge'
CheckPermutation(string1, string2)
