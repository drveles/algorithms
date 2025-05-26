class Solution:
    def __init__(self):
        self.result = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if low <= root.val <= high:
            self.result += root.val
        if root.left:
            self.rangeSumBST(root.left, low, high)
        if root.right:
            self.rangeSumBST(root.right, low, high)
        return self.result
