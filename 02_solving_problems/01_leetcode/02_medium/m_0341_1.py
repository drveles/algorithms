# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def recursion(temp_el):
            res = []
            for el in temp_el:
                if not el.isInteger():
                    res.extend(recursion(el.getList()))   
                else:
                    res.append(el.getInteger())
            return res
        
        self.array = recursion(nestedList)
        self.lenght = len(self.array)
        self.position = 0
    

    def next(self) -> int:
        self.position += 1
        return self.array[self.position - 1]
            
    
    def hasNext(self) -> bool:
        return True if self.position < self.lenght else False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

#OK, 60%, 69%