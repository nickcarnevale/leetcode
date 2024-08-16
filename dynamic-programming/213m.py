# https://leetcode.com/problems/house-robber-ii/description/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0

        def help(arr):
            rob1, rob2 = 0, 0

            for n in arr:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2

        return max(help(nums[1:]),help(nums[:-1]))