# https://leetcode.com/problems/valid-parentheses/description/ 

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        n = len(s)

        # edge case
        if(n == 1):
            return False

        for i in range(n):
            if s[i] == ")" :
                if stack[-1] == "(":
                    stack.pop()
            elif s[i] == "]" :
                if stack[-1] == "[":
                    stack.pop()
            elif s[i] == "}" :
                if stack[-1] == "{":
                    stack.pop()
            else:
                stack.append(s[i])
            
        if len(stack) == 0:
            return True

        return False
            

            