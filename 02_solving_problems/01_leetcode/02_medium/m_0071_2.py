class Solution:
    def simplifyPath(self, path: str) -> str:
        res_stack = []
        
        for el in path.split("/"):
            if el == "..":
                if res_stack:
                    res_stack.pop()
            elif el not in ".":
                res_stack.append(el)

        return "/" + "/".join(res_stack)
