class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            print(tuple(count))
            li[tuple(count)].append(s)
        return li.values()