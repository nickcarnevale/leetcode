# https://leetcode.com/problems/remove-duplicates-from-sorted-array/ 

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 1,2,2,3,4,4,4,5,6

        # approach
        # sliding window
        

        n = len(nums)

        if n == 0:
            return 0

        k = 1

        for i in range(1,n):
           if(nums[i] != nums[i-1]):
                nums[k] = nums[i]
                k += 1

        return k








        
        