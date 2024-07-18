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
        if n == 1 :
            return False

        if s[0] == ")" or s[0] == "]" or s[0] == "}":
            return False

        if s[-1] == "(" or s[-1] == "[" or s[-1] == "{":
            return False

        for i in range(n):
            if s[i] == ")" :
                if len(stack) > 0:
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            elif s[i] == "]" :
                if len(stack) > 0:
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            elif s[i] == "}" :
                if len(stack) > 0:
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(s[i])
            
        if len(stack) == 0:
            return True

        return False