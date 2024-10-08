# https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        hset = set()
        r = []
        n = len(nums)
        nums.sort()

        # approach
        # outer loop tracks the first of four in the sum
        for one in range(n - 3):

            # inner loop to track the second of four in the sum
            # start with 1 after one to eliminate duplicates
            for two in range(one + 1, n - 2):
            
                three = two + 1
                four = n - 1    

                while three < four:
                    sum = nums[one] + nums[two] + nums[three] + nums[four]

                    if sum < target:
                        three += 1
                    elif sum > target:
                        four -= 1
                    else:
                        l = (nums[one], nums[two], nums[three], nums[four])
                        if l in hset:
                            pass  # Already in the set, skip
                        else: 
                            r.append([nums[one], nums[two], nums[three], nums[four]])    
                            hset.add(l)
                            
                        while three < four and nums[three] == nums[three + 1]:
                            three += 1  # Skip duplicates
                        while three < four and nums[four] == nums[four - 1]:
                            four -= 1  # Skip duplicates
                        three += 1
                        four -= 1
        return r




            

            

        



            

            
            
