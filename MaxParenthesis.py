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
        return -1
    else:
        return stack.pop()

def maxDepth(string):
    count = 0
    maxcount = 0
    stack = createStack()
    length =  len(string)
    for i in range(0, length):
        if string[i] == '(':
            count = count + 1
            if maxcount<count:
                maxcount = count
        elif string[i] == ')':
            count = count - 1
    if count==0:
        return maxcount
    else:
        return -1

# Driver program 
s = "( ((X)) (((Y))) )"
print(maxDepth(s))
