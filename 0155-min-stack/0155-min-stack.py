class MinStack:

    def __init__(self):
        self.st = []
    
    def push(self, value: int) -> None:
        if not self.st:
            self.st.append((value,value))
        else:
            curr_min = min(value, self.st[-1][1])
            self.st.append((value,curr_min))
    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()