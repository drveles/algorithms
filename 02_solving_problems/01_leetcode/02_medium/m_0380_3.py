class RandomizedSet:
    def __init__(self):
        self.arr = list()
        self.dct = dict()

    def insert(self, val: int) -> bool:
        if val in self.dct:
            return False
        
        self.dct[val] = len(self.arr)
        self.arr.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.dct:
            return False

        idx = self.dct[val]
        last_val = self.arr[-1]
        self.arr[-1], self.arr[idx] = self.arr[idx], self.arr[-1]
        self.arr.pop()
        self.dct[last_val] = idx
        del self.dct[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
