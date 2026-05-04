class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for st in strs:
            s += str(len(st)) + '!' + st
        return s

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '!':
                j += 1
            st_len = int(s[i:j])
            i = j+1
            j = i+st_len
            output.append(s[i:j])
            i = j

        return output