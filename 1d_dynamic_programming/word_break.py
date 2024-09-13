from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        STR_LEN = len(s)
        # Store all of the words in a dict
        word_set = {""}
        for string in wordDict:
            word_set.add(string)
        
        # <index, Set<length of diff words we can have at this index>
        word_map = {} 
        for i in range(STR_LEN):
            word_map[i] = {0}
        
        # Populate word_map
        for l in range(STR_LEN):
            for r in range(STR_LEN):
                curr_str = s[l:r+1]
                if curr_str in word_set:
                    word_map[l].add(len(curr_str))
        for i in range(STR_LEN):
            word_map[i].remove(0)

        # <current_index, all possible combination sums up to that point>
        dp = [False]*STR_LEN
        for word_len in word_map[0]:
            dp[word_len - 1] = True

        for i in range(1, STR_LEN):
            if dp[i-1]:
                for word_len in word_map[i]:
                    dp[i + word_len - 1] = True

        return dp[STR_LEN-1]