# https://leetcode.com/problems/maximum-subarray/description/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # nums always has 1 element

        c = 0
        m = nums[0]

        for n in nums:
            c += n
            m = max(m, c)
            if c < 0:
                c = 0

        return m

        