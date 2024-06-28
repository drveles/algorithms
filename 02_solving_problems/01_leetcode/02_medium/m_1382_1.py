# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        temp_list = []
        def bfs(node):
            if not node: 
                return
            
            temp_list.append(node.val)
            bfs(node.left)
            bfs(node.right)
        
        bfs(root)
        temp_list.sort()

        def top_down(left_id, right_id):
            if left_id > right_id: 
                return None

            mid = (left_id + right_id) // 2
            root = TreeNode(temp_list[mid])
            root.left = top_down(left_id, mid - 1)
            root.right = top_down(mid + 1, right_id)

            return root


        return top_down(0, len(temp_list) - 1)

# OK , 88% , 79%    