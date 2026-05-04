class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []


        digitMap = {2: ['A', 'B', 'C'],
                    3: ['D', 'E', 'F'],
                    4: ['G', 'H', 'I'],
                    5: ['J', 'K', 'L'],
                    6: ['M', 'N', 'O'],
                    7: ['P', 'Q', 'R', 'S'],
                    8: ['T', 'U', 'V'],
                    9: ['W', 'X', 'Y', 'Z']}
        
        ret = []

        def backtrack(i, temp):
            if i == len(digits):
                ret.append(temp.lower())
                return
            
            for c in digitMap[int(digits[i])]:
                backtrack(i + 1, temp + c)
            
            return
        
        backtrack(0, "")

        return ret
