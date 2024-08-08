# https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Binary Search

        left = 0
        n = len(nums)
        right = n-1
        mid = (left + right) // 2

        if target > nums[-1]:
            return n
        elif target < nums[0]:
            return 0

        while left <= right:
            
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
            
        return left