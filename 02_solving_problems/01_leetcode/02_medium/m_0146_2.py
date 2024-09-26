from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.ordict = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.ordict:
            self.ordict.move_to_end(key)
            return self.ordict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.ordict:
            self.ordict.move_to_end(key)
        self.ordict[key] = value
        if len(self.ordict) > self.capacity:
            self.ordict.popitem(last=False)
