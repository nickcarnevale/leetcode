# https://leetcode.com/problems/two-sum/

# BRUTE FORCE
# TWO POINTERS
# O(n^2) worst case

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # negative numbers? cannot eliminate numbers greater than target
        # 0, cannot eliminate numbers equal to target

        dif = 0 # need to keep track of the difference between the target and the first pointer
        l = 0 # left pointer
        r = 1 # right pointer

        while True: # infinite loop to iterate until answer is found
        
            # logic, looking for target - nums[l] in nums[j]
            # if j >= len(nums), increment l and start again

            dif = target - nums[l]
            if nums[r] == dif:
                return [l,r]
            
            if (1 + r) == len(nums):
                l += 1
                r = l

            r += 1

# HASH MAP

class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Logic, insert each value into the hashmap and 
        # check if its compliment is already in the map
        # if it is return the indicies, if not continue adding to the hash map

        m = {}
        n = len(nums) 
        
        for i in range(n):
            dif = target - nums[i]
            
            if dif in m:
                return [i, m[dif]]

            m[nums[i]] = i  # add each pair to the map


        



            
