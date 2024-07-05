# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inf = sys.maxsize

        def dfs_check(l, node, r):
            if not node:
                return True
            
            if l < node.val < r:
                return dfs_check(l, node.left, node.val) and dfs_check(node.val, node.right, r)
            else:
                return False

        return dfs_check(-inf, root, inf)

#OK, 86%, 6%