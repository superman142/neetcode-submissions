class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)

        for word in strs:
            count = [0]*26

            for c in word:
                count[ord(c) - ord('a')] += 1

            ret[tuple(count)].append(word)
        
        return [v for v in ret.values()]
