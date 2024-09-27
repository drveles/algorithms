class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def bfs(node_left, node_right):
            if not node_left and not node_right:
                return True
            if not node_left or not node_right:
                return False
            if node_left.val != node_right.val:
                return False
            
            return bfs(node_left.right, node_right.left) and bfs(node_left.left, node_right.right)
        
        return bfs(root.left, root.right)
