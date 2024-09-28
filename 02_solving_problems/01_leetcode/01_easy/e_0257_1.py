# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        
        def dfs(node: Optional[TreeNode], curr_path: str): 
            if not node.left and not node.right:
                result.append(f"{curr_path}{node.val}")
            
            if node.left:
                dfs(node.left, f"{curr_path}{node.val}->")
            if node.right:
                dfs(node.right, f"{curr_path}{node.val}->")

        dfs(root, "")
        return result
