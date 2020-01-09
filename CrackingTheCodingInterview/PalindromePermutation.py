def PalindromePermutation(string1):
    Dict = {}
    string1 = string1.lower()
    for i in string1:
        if i == " ":
            continue
        if i in Dict:
            Dict[i] =  Dict[i] + 1
        else:
            Dict[i] = 1
    
    odd = 0
    for j in Dict.values():
        if j%2==0:
            continue
        else:
            odd = odd + 1
        if odd>=2:
            return False
    return True

string1 = "Tact Coa"
PalindromePermutation(string1)
