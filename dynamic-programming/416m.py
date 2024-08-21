# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        numsTotal = sum(nums)
        target = numsTotal // 2
        dp = {}

        if sum(nums) % 2 == 1:
            return False

        def dfs(i, total):
            if total == target:
                return True
            
            if i == n:
                return False

            if (i, total) in dp:
                return dp[(i,total)]

            dp[(i,total)] = dfs(i+1, total) or dfs(i+1, total + nums[i])
            return dp[(i,total)]

        return dfs(0,0)


            



            
        

        
        