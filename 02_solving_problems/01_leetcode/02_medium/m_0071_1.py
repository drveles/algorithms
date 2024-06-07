class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        ans_str = ""

        for step in path:
            if not step:
                continue
            if step == "..":
                if stack:
                    stack.pop(-1)
            elif step == ".":
                continue
            else: 
                stack.append(step)
        
        for step in stack:
            ans_str += "/" + step

        if not ans_str:
            return '/'

        return ans_str

#Ok, 80%, 79%