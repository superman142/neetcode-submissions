class Solution:
    def simplifyPath(self, path: str) -> str:
        ret = []
        i = 0
        
        paths = path.split('/')

        for val in paths:
            if val == "" or val == ".":
                continue
            
            if val == "..":
                if ret:
                    ret.pop()
            else:
                ret.append(val)
        
        return "/" + "/".join(ret)

