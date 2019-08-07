def IsOperand(x, precedence):
    for i in precedence:
        if i==x:
            return False
    else:
        return True


def InfixToPostfix(exp):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3, '(': 0, ')':0}
    precedenceArr = []
    for element in exp:
        if (IsOperand(element, precedence)):
            print(element, end = '')
        else:
            if (len(precedenceArr)==0):
                precedenceArr.append(element)
            elif element =='(':
                precedenceArr.append(element)
            elif element == ')':
                while(precedenceArr[-1]!='('):
                    print(precedenceArr.pop(), end = '')
                precedenceArr.pop()
            elif (precedence[element]>precedence[precedenceArr[-1]]):
                precedenceArr.append(element)
            else:
                while ((precedence[element]<=precedence[precedenceArr[-1]])) :
                    print(precedenceArr.pop(), end = '')
                    if len(precedenceArr)==0:
                        break
                precedenceArr.append(element)
    while(len(precedenceArr)!=0):
        print(precedenceArr.pop(), end = '')
  

exp = 'a+b*(c^d-e)^(f+g*h)-i'
InfixToPostfix(exp)
