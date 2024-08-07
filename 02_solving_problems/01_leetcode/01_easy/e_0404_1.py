class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ctr = 0

        if root.left and not root.left.left and not root.left.right:
            ctr += root.left.val

        return ctr + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


# OK, 27%, 31%
