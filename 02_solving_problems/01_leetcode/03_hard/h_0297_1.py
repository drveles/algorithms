class Codec:
    def serialize(self, root):
        if not root:
            return "None"

        return str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))

    def deserialize(self, data):
        data = data.split(",")

        def bfs():
            pop_d = data.pop(0)
            if pop_d == "None":
                return None
            root = TreeNode(pop_d)
            root.left = bfs()
            root.right = bfs()
            return root
            
        return bfs()
