# https://leetcode.com/problems/target-sum/

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # at each integer, two decisions, + or -
        dp = {}

        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0

            if (i, total) in dp:
                return dp[(i, total)]

            # Calculate number of ways by including both + and - operations
            add = dfs(i + 1, total + nums[i])
            subtract = dfs(i + 1, total - nums[i])

            dp[(i, total)] = add + subtract

            return dp[(i, total)]

        return dfs(0, 0)

            

            


        