class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        if self.min:
            self.min.append(min(val, self.min[-1]))
        else:
            self.min.append(val)
        self.stack.append(val)
        
    def pop(self) -> None:
        self.min.pop()
        return self.stack.pop()
    

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()