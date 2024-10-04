# Хочу поднимать наверх только максимальный путь в текущей ноде и обновлять максимум.
# Оказывется, не обязательно доходить до конца дерева, можно оставновиться в ноде и не идти в ее потомков.
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = -sys.maxsize
        def checker(node):
            if not node:
                return 0
            
            left = max(checker(node.left), 0)
            right = max(checker(node.right), 0)
            self.result = max(self.result, node.val + left + right)

            return max(left, right) + node.val
        
        checker(root)
        
        return self.result
