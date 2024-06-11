# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(current_node, temp_deep):
            if not current_node:
                return temp_deep
            
            return max(dfs(current_node.left, temp_deep + 1), dfs(current_node.right, temp_deep + 1))

        return dfs(root, 0)   

#OK 75%, 7%