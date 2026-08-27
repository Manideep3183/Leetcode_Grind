class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    def remove(self, node):
        next = node.next
        prev = node.prev
        prev.next = next
        next.prev = prev

    def insert(self, node):
        prev = self.right.prev
        next = self.right

        node.next = next
        node.prev = prev

        prev.next = node
        next.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key,value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)