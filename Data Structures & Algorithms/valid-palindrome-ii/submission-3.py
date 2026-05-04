class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(l, r):

            while l < r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True

        l = 0
        h = len(s) - 1

        while l < h:
            if s[l] != s[h]:
                return is_palindrome(l, h - 1) or is_palindrome(l + 1, h)
            l += 1
            h -= 1
          
        return True
            
            