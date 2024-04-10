# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
class Solution:
    def swap(self, root):
        if root:
            root.left, root.right = root.right, root.left

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)
            self.swap(root)

        return root

#OK 76%, 34%