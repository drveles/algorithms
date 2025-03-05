class MyIterator:
    def __init__(self):
        self.arr = [1 + idx for idx in range(10)]
        self.ptr = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.ptr < len(self.arr):
            self.ptr += 1
            return self.arr[self.ptr - 1]
        else:
            raise StopIteration


for obj in MyIterator():
    print(obj)
