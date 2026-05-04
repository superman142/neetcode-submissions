class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""

        for word in strs:
            ret += (str(len(word)) + "#" + word)
        
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0 

        while i < len(s):
            count = ""
            while s[i] != "#":
                count += s[i]
                i += 1
            
            i += 1
            ret.append(s[i: i + int(count)])

            i += int(count)
        
        return ret
            


            
        



