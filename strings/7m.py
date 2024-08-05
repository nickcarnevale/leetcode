# https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = x < 0
        r = str(abs(x))[::-1]
        reversed_int = int(r)

        if reversed_int > 2**31 - 1:
            return 0
        
        return -reversed_int if neg else reversed_int
