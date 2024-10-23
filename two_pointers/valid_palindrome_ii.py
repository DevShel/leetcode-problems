# https://leetcode.com/problems/valid-palindrome-ii

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1: return False
        elif len(s) == 2: return True
        if s == s[::-1]: return True # Check if already a palindrome
    
        lPtr, rPtr = 0,len(s) - 1

        while(s[lPtr] == s[rPtr]):
            lPtr += 1
            rPtr -= 1

        # Find the first element without a corresponding mirror, then check if palindrome after removal
        # Must do for both sides
        if s[lPtr] != s[rPtr]:
            testRemoving_lPtr = s[:lPtr] + s[lPtr+1:] # Originally indexed to -1... don't make this mistake in the future
            testRemoving_rPtr = s[:rPtr] + s[rPtr+1:]
            if testRemoving_lPtr == testRemoving_lPtr[::-1]: return True
            elif testRemoving_rPtr == testRemoving_rPtr[::-1]: return True

        return False