from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # A palindrome partitioning is when you can use every character, and return these substrings in way where that substring is a palindrome
        global_list = []
        self.recursive_backtrack(s, 0, [], global_list)
        return global_list

        # All possible: makes me think recursive backtracking
        # Get list of all possible palidnromes at this location, then call a new recursive call with a new local that includes that palindrome
    
    def recursive_backtrack(self, s, i, local, global_list):
        if (i < len(s)):
            add_curr_element = local.copy()
            add_curr_element.append(s[i])
            self.recursive_backtrack(s, i+1, add_curr_element, global_list)

            pals_at_i = self.all_palindromes_at_index(s, i)
            for pal in pals_at_i:
                add_curr_pal = local.copy()
                add_curr_pal.append(pal)
                self.recursive_backtrack(s, i + len(pal), add_curr_pal, global_list)
        else:
            global_list.append(local)
       
    def all_palindromes_at_index(self, s, i):
        palindrome_list = []
        # For every possible substring starting at curr index
        for j in range(i + 1, len(s)):
            # Determine if this substring is a palindrome
            is_palindrome = True
            l_ptr, r_ptr = i, j
            while (r_ptr > l_ptr):
                if (s[l_ptr] != s[r_ptr]):
                    is_palindrome = False
                    break
                r_ptr = r_ptr - 1
                l_ptr = l_ptr + 1

            if (is_palindrome): palindrome_list.append(s[i:j+1])
            print (palindrome_list)
        return palindrome_list