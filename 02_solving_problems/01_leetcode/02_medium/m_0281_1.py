"""
Given two vectors of integers v1 and v2, implement an iterator to return their elements alternately.

Implement the ZigzagIterator class:

ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2.
boolean hasNext() returns true if the iterator still has elements, and false otherwise.
int next() returns the current element of the iterator and moves the iterator to the next element.

# Хочу при инициализации смерджить эти два листав используя зигзаг
# hasNext будет смотреть индекс не вышел за пределы получившегося массива.
# next будет отдавать элементы по очереди

Чтобы смерджить списки буду обходить массивы в двух циклах.
"""

class ZigzagIterator():
    def __init__(self, list1: list[int], list2: list[int]):
        self.array = []
        self.current_idx = 0

        temp_idx = 0
        while temp_idx < min(len(list1), len(list2)):
            for list_id in range(2):
                if list_id:
                    self.array.append(list2[temp_idx])
                else:
                    self.array.append(list1[temp_idx])
            temp_idx += 1

        if len(list1) > temp_idx:
            self.array.extend(list1[temp_idx:])
        if len(list2) > temp_idx:
            self.array.extend(list2[temp_idx:])


    def hasNext(self) -> bool:
        if self.current_idx < len(self.array):
            return True
        
        return False


    def next(self):
        if self.hasNext():
            self.current_idx += 1
            return self.array[self.current_idx - 1]
    

if __name__ == "__main__":
    z = ZigzagIterator([1,2,3,4], [5,6])
    print(z.next())
    print(z.next())
    print(z.next())
    print(z.next())
    print(z.next())
    print(z.next())
    print(z.next())