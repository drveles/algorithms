class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution():
    def lowestCommonAncestor(self, p: Node, q: Node):
        one, two = p, q

        while one != two:
            one = one.parent if one else q
            two = two.parent if two else p

        return one
