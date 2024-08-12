# https://leetcode.com/problems/unique-paths-ii/description/

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n, m = len(obstacleGrid), len(obstacleGrid[0])

        cache = [ [0]*m for _ in range(n) ]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if(obstacleGrid[i][j] == 1):
                    #there is a boulder
                    cache[i][j] = 0
                else:
                    # No boulder
                    if i == n-1 and j == m-1:
                        # The bottom-right corner
                        cache[i][j] = 1
                    else:
                        if i+1 < n:
                            cache[i][j] += cache[i+1][j]
                        if j+1 < m:
                            cache[i][j] += cache[i][j+1]

        return cache[0][0]