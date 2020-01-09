def URLify(string1, TrueLength):
    string2 = ""
    for i in range(TrueLength):
        if string1[i]==" ":
            string2 = string2 + "%20"
        else:
            string2 = string2 + string1[i]       
    return string2


string1 = "Mr John Smith          "
URLify(string1, 13)
