# https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        index = {}

        right = 0
        while right < len(nums):
            num = nums[right]
            if num in index:
                if abs(index[num]-right) <= k:
                    return True
                else:
                    index[num] = right
            else:
                index[num] = right
            right += 1
        return False

        