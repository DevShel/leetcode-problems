# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Very similar to balance parentheses problem: use a stack
        output_str = ""
        num_removed = 0
        stack = []
        for i,c in enumerate(s):
            if c == ')':
                # If the stack is empty, or we don't have a balancer
                if len(stack) == 0: 
                    output_str += "!"
                    continue
                # If there is a balancer, then pop the balancer
                else: stack.pop()
            if c == '(': 
                stack.append(('(', i))
            output_str += c
        
        # Mark all of the elements left over in the stack as invalid
        while(len(stack) > 0):
            replace_index = stack.pop()[1]
            output_str = output_str[0:replace_index] + "!" + output_str[replace_index + 1: len(output_str)]

        # Remove marked elements from the stack
        return output_str.replace("!", '')