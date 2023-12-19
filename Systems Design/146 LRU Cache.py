#this implementaiton is not correct
#Watch Systems design foundation video 27. LRU Cache where Omkar implemented LRU Cache with
#   a hashtable and a doubly linked list.
#leet code solution (someone's) from below works
class LRUCache:

    def __init__(self, capacity: int):
        import collections
        self.cache = collections.deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in [key for key, value in self.cache]:
            return_item = self.cache.pop()
            self.cache.appendleft(return_item)
            return return_item[1]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity:
            self.cache.pop()
        self.cache.appendleft((key, value))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

lRUCache = LRUCache(2)
print(lRUCache.cache)
lRUCache.put(1, 1) #cache is {1=1}
print(lRUCache.cache)
lRUCache.put(2, 2) #cache is {1=1, 2=2}
print(lRUCache.cache)
print(lRUCache.get(1)) #return 1
print(lRUCache.cache)
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.cache)
print(lRUCache.get(2)) # returns -1 (not found)
print(lRUCache.cache)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.cache)
print(lRUCache.get(1)) # return -1 (not found)
print(lRUCache.cache)
print(lRUCache.get(3)) # return 3
print(lRUCache.cache)
print(lRUCache.get(4)) # return 4
print(lRUCache.cache)

def LRU_Cache():
    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.capacity = capacity
        self.values = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        else:
            self.values[key] = self.values.pop(key)
            return self.values[key]


    def put(self, key: int, value: int) -> None:
        if key not in self.values:
            if len(self.values) == self.capacity:
                self.values.popitem(last=False)
        else:
            self.values.pop(key)
        self.values[key] = value