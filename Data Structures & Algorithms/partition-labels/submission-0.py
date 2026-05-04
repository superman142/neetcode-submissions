class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idxMap = defaultdict(list)

        for i, c in enumerate(s):
            if c  not in idxMap:
                idxMap[c] = [i, i]
            
            idxMap[c][-1] = i
        
        ret = []
        i = 0
        last = 0
        prev = 0
        while i < len(s):
            letter = s[i]
            last = max(last, idxMap[letter][-1])
            
            if last <= i:
                ret.append(last - prev + 1)
                prev = i + 1
            i += 1

        return ret
            
