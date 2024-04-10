def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    count = 0
    if not root.left and not root.right:
        return count
    
    def deep(root, count):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return deep(root.left, 2) + deep(root.right, 2)
    
    return deep(root, count)

#WA