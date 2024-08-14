# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = ''.join(c.lower() for c in s if c.isalpha() or c.isnumeric())
        n = len(s)
        mid = n // 2
        print(s)
        for i in range(mid):
            if s[i] != s[n-1-i]:
                return False

        return True