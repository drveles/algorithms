class RandomizedSet:

    def __init__(self):
        self.main_set = set()

    def insert(self, val: int) -> bool:
        if val in self.main_set:
            return False
        
        self.main_set.add(val)
        
        return True

    def remove(self, val: int) -> bool:
        if not val in self.main_set:
            return False

        self.main_set.discard(val)
        
        return True

        
    def getRandom(self) -> int:
        from random import choice
        return choice(list(self.main_set))
        


# brute force