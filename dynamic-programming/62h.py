# https://leetcode.com/problems/unique-paths/description/

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        cache = [[1] * m for _ in range(n)]

        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                cache[i][j] = cache[i+1][j] + cache[i][j+1]

        return cache[0][0]

        