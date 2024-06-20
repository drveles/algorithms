# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = float("-inf")


    def depth_max(self, node) -> int:
        if not node: 
            return 0

        left = self.depth_max(node.left)
        right = self.depth_max(node.right)
        self.result = max(self.result, node.val + right + left)

        return max(node.val + max(left, right), 0)


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.depth_max(root)

        return self.result

#OK, 92%, 88%