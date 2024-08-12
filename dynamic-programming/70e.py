# https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        calc = []
        calc.append(1)
        calc.append(1)

        if n == 1:
            return 1
        if n == 0:
            return 0

        for i in range(2, n):
            first = i-2
            second = i-1
            calc.append(calc[first] + calc[second])

        return calc[-2] + calc[-1]



        