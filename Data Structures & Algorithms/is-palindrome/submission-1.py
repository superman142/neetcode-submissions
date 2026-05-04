class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = ""
        for i in range(len(s)):
            if self.isAlphaNum(s[i]):
                cleanS += s[i].lower()
        print(cleanS)
        return cleanS == cleanS[::-1]
    
    def isAlphaNum(self, c) -> bool:
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))
    