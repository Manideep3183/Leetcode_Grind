from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache.pop(key) 
        self.cache[key] = value
        return self.cache[key]
    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key) 
        elif len(self.cache) >= self.cap:
            self.cache.popitem(last=False)
        self.cache[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)