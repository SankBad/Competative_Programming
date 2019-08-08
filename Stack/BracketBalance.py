def BracketBalance(str):
    stack = []
    ParaArr = { '(': 1, ')' : 1, '{': 2, '}': 2, '[': 3, ']': 3}
    for i in str:
        if (i == '(' or i == '{' or i == '['):
            stack.append(i)
        else:
            if len(stack) == 0:
                return 'not balanced'
            temp =  stack.pop()
            if ParaArr[temp] == ParaArr[i]:
                a = 1
            else:
                return 'not balanced'
    if len(stack)== 0:
        return 'balanced'
    else:
        return 'not balanced'
    

expr = "{()}[]{"
print(BracketBalance(expr))
