class Solution:
    def encodeWord(self, word: str) -> str:
        count = [0]*26
        ret = ""

        for c in word:
            count[ord(c) - ord('a')] += 1

        for c in count:
            ret += (str(c) + str("."))

        return ret


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()

        for word in strs:
            encoded = self.encodeWord(word)
            groups[encoded] = groups.get(encoded,[]) + [word]

        ret = []

        for val in groups.values():
            ret.append(val)
        
        return ret


