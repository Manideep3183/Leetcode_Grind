class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)
        self.history = {0 : self.curr}
        self.curridx = 0
        self.maxidx = 0

    def visit(self, url: str) -> None:
        newnode = Node(url)
        prevnode = self.history[self.curridx]

        prevnode.next = newnode
        newnode.prev = prevnode

        self.curridx += 1
        self.history[self.curridx] = newnode
        self.maxidx = self.curridx

    def back(self, steps: int) -> str:
        self.curridx = max(0, self.curridx - steps)
        return self.history[self.curridx].val


    def forward(self, steps: int) -> str:
        self.curridx = min(self.curridx + steps, self.maxidx)
        return self.history[self.curridx].val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)