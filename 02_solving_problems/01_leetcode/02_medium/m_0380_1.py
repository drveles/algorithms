class RandomizedSet:
    def __init__(self):
        self.dct = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.dct:
            return False
        self.dct[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.dct:
            return False
        last_val = self.arr[-1]
        val_id = self.dct[val]
        self.dct[last_val] = val_id
        self.arr[val_id] = last_val
        self.arr.pop()
        del self.dct[val]
        return True
        

    def getRandom(self) -> int:
        import random
        return random.choice(self.arr)
        
#OK, 85%, 68%