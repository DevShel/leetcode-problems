# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_map = {}

        for c in s:
            if c in s_map: s_map[c] = s_map[c] + 1 # increase count of char in word
            else: s_map[c] = 1 # set count of char to 1
        
        for c in t:
            if c in s_map:
                if s_map[c] == 1: s_map.pop(c) # if it is the last char, pop it
                else: s_map[c] = s_map[c] - 1 # reduce the frequency of the char by 1
        
        return not s_map