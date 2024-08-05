# https://leetcode.com/problems/reverse-string/

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        n = len(s)
        half = n//2
        
        for i in range(half):
            #switch i and n-i
            copy = s[n-1-i]
            s[n-1-i] = s[i]
            s[i] = copy

        return s
