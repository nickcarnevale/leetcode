# https://leetcode.com/problems/last-stone-weight-ii/description/

class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        # Return the smallest possible weight of the left stone. If there are no stones left, return 0.

        dp = {}
        stoneSum = sum(stones)
        target = ceil(stoneSum / 2)

        def dfs(i, total):

            if total >= target or i == len(stones):
                return abs(total - (stoneSum - total))
            
            if (i, total) in dp:
                return dp[(i,total)]

            dp[i, total] = min(dfs(i+1, total), dfs(i+1, total + stones[i]))

            return dp[i,total]

        return dfs(0,0)







        