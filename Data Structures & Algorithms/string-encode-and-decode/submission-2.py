class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""

        for word in strs:
            ret += (str(len(word)) + "#")
            ret += word
        
        return ret

    def decode(self, s: str) -> List[str]:
        i = 0
        ret = []

        while i < len(s):
            count = ""
            while i < len(s) and s[i] != '#':
                count += s[i]
                i += 1
            
            i += 1

            count = int(count)
            ret.append(s[i: i + count])
            i += count

        return ret

