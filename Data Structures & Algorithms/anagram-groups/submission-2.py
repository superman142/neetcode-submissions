class Solution:

    def getKey(self, word):
        count = [0]*26

        for c in word:
            count[ord(c) - ord("a")] += 1

        ret = ""
        for c in count:
            ret += (str(c) + "-")
        return ret

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        retMap = {}

        for word in strs:
            key = self.getKey(word)
            retMap[key] = retMap.get(key, []) + [word]
        
        return [v for v in retMap.values()]

        