class MinStack(object):

    def __init__(self):
        self.s = []
    def push(self, value):
        if not self.s:
            self.s.append((value,value))
        else:
            currmin = min(value, self.s[-1][1])
            self.s.append((value,currmin))
    def pop(self):
        self.s.pop()
    def top(self):
        return self.s[-1][0]
    def getMin(self):
        return self.s[-1][1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()