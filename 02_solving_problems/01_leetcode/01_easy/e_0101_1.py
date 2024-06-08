# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(leftnode, rightnode) -> bool:
            if not leftnode and not rightnode:
                return True
            if not leftnode or not rightnode:
                return False

            if leftnode.val != rightnode.val:
                return False

            return dfs(leftnode.left, rightnode.right) and dfs(leftnode.right, rightnode.left)
        
        return dfs(root.left, root.right)

#OK, 54%, 54%