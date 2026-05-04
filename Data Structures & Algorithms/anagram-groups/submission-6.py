class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list)

        def reduce(word):
            count = [0]*26

            for c in word:
                count[ord(c) - ord('a')] += 1
            
            return tuple(count)

        for word in strs: 
            anaMap[reduce(word)].append(word)

        return [v for v in anaMap.values()]