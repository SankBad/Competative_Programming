class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.myStack =  []
        

    def push(self, x: int) -> None:
        return self.myStack.append(x)
        

    def pop(self) -> None:
        return self.myStack.pop()
        
        

    def top(self) -> int:
        return self.myStack[-1]
        

    def getMin(self) -> int:
        return min(self.myStack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
