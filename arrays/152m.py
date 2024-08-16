# https://leetcode.com/problems/maximum-product-subarray/

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        mx = mn = result = nums[0]

        for n in nums[1::]:
            if n < 0:
                mx, mn = mn, mx

            mx = max(n, mx*n)
            mn = min(n, mn*n)
            result = max(result, mx)

        return result