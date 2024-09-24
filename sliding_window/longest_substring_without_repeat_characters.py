# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        if (s_len == 0 or s_len == 1): return s_len

        running_max = 1
        window = set()
        window.add(s[0])
        l, r = 0, 1
        
        while (r < s_len):
            while r < s_len and s[r] not in window: # Expand window to the right until we hit repeat
                window.add(s[r])
                r += 1
            
            running_max = max(running_max, r - l)

            while r < s_len and s[r] in window: # Remove from left until we get to repeating char, then skip it
                window.remove(s[l])
                l += 1

        return running_max
