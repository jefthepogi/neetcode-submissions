class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        s = "".join([char for char in s if char.isalnum()])
        length = len(s)
        
        R = len(s) - 1
        for L in s:
            if s[R] != L:
                return False
            R -= 1

        return True