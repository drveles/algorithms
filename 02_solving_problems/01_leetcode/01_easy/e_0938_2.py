class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0

        def bfs(node):
            if not node:
                return

            nonlocal result

            if low <= node.val <= high:
                result += node.val
            if low < node.val:
                bfs(node.left)
            if node.val < high:
                bfs(node.right)

        bfs(root)
        return result