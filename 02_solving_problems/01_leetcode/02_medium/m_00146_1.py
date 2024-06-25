class LRUCache:

    def __init__(self, capacity: int):
        self.dct = {}
        self.queue = []
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.dct:
            self.queue.append(self.queue.pop(self.queue.index(key)))
        return self.dct.get(key, -1)

        

    def put(self, key: int, value: int) -> None:
        if key in self.dct:
            self.dct[key] = value
            self.queue.append(self.queue.pop(self.queue.index(key)))
        else:
            self.dct[key] = value
            self.queue.append(key)
            if len(self.queue) > self.capacity:
                del self.dct[self.queue.pop(0)]


#OK, 6%, 56%