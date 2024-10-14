#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def is_valid(self, s: str) -> bool:
        open_to_close_bracket: dict[str, str] = { '(': ')', '{': '}', '[': ']' }

        stack: list[str]= []

        for bracket in s:
            if bracket in open_to_close_bracket:
                stack.append(open_to_close_bracket[bracket])
            elif not stack or stack.pop() != bracket:
                return False
            
        return not stack
