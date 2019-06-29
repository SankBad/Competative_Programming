def createStack():
    stack = []
    return stack

def push(stack, x):
    stack.append(x)

def size(stack): 
    return len(stack)

def isEmpty(stack):
    if(size(stack)==0):
        return True
    else:
        return False

def pop(stack):
    if(isEmpty(stack)):
        return
    else:
        return stack.pop()    

def reverse(string):
    length = len(string)
    print(length)
    stack = createStack()
    for i in range(0, length):
        push(stack, string[i])
    
    string1="" 
    
    for i in range(0, length):
        temp = pop(stack)
        string1 = string1+temp
    
    return string1   
    



string="GeeksQuiz"
string = reverse(string) 
print("Reversed string is " + string) 
