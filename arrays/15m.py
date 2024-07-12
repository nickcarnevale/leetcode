# https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # similar to two sum approach
        # cannot contain duplicates is key
        # going to use a dictionary to store values

        hset = set()
        r = []
        n = len(nums)
        left = 0
        middle = n // 2
        right = n - 1

        #edge cases
        if n < 3:
            return r
        elif n == 3:
            if (nums[left] + nums[middle] + nums[right]) == 0 :
                r.append([nums[left], nums[middle], nums[right]]) 
                return r

        # if there are 4 or more values

        # sort the array: O(n logn)
        nums.sort()

        # with a sorted array, you can compare values less than 0 and greater than 0 without comparing all of them
        while True:
            
            # find current indicies sum
            sum = (nums[left] + nums[middle] + nums[right])

            # check if the current indicies add to 0
            if sum == 0 :
                if (nums[left], nums[middle], nums[right]) in hset:
                   middle = n // 2 
                else:
                    r.append([nums[left], nums[middle], nums[right]])
                    hset.add( (nums[left], nums[middle], nums[right]) )

    
                # reset middle and move left and right in one
                middle = n // 2

                # move the right one over if its larger than the absolute value of the left one
                if abs(nums[left]) < nums[right]:
                    right -= 1
                elif abs(nums[left]) > nums[right]:
                    left += 1
                else: 
                    # need the case when they are equal: need to check both sides
                    # recursive
                    # use helper functions because they only change the variable locally
                    def right(right, left, middle, r, hset):
                        right -= 1

                        while True:
                            sum = (nums[left] + nums[middle] + nums[right])
                            if sum == 0 :
                                if (nums[left], nums[middle], nums[right]) in hset:
                                    middle = n // 2 
                                else:
                                    r.append([nums[left], nums[middle], nums[right]])
                                    hset.add( (nums[left], nums[middle], nums[right]) )
                                middle = n // 2
                                right -= 1
                                if left == middle:
                                    break
                                elif right == middle:
                                    break
                            elif sum > 0:
                                if (middle - 1) != left:
                                    middle -= 1 
                                    if (nums[left] + nums[middle] + nums[right]) < 0: 
                                        break
                                else: 
                                    middle = n // 2
                                    right -= 1
                                    if right == middle:
                                        break
                            
                            else:
                                if (middle + 1) != right:
                                    middle += 1 
                                if (nums[left] + nums[middle] + nums[right]) > 0: 
                                        break
                                else: 
                                    middle = n // 2
                                    left += 1
                                    if left == middle:
                                        break
                    def left(right, left, middle, r, hset):
                        left += 1
                        while True:
                            sum = (nums[left] + nums[middle] + nums[right])
                            if sum == 0 :
                                if (nums[left], nums[middle], nums[right]) in hset:
                                    middle = n // 2 
                                else:
                                    r.append([nums[left], nums[middle], nums[right]])
                                    hset.add( (nums[left], nums[middle], nums[right]) )
                                middle = n // 2
                                left += 1
                                if left == middle:
                                    break
                                elif right == middle:
                                    break
                            elif sum > 0:
                                if (middle - 1) != left:
                                    middle -= 1 
                                    if (nums[left] + nums[middle] + nums[right]) < 0: 
                                        break
                                else: 
                                    middle = n // 2
                                    right -= 1
                                    if right == middle:
                                        break
                            
                            else:
                                if (middle + 1) != right:
                                    middle += 1 
                                if (nums[left] + nums[middle] + nums[right]) > 0: 
                                        break
                                else: 
                                    middle = n // 2
                                    left += 1
                                    if left == middle:
                                        break
                    right(right, left, middle, r, hset)
                    left(right, left, middle, r, hset)
                if left == middle:
                    break
                elif right == middle:
                    break
            
            # if the sum is greater than zero move the middle left
            elif sum > 0:
                if (middle - 1) != left:
                    middle -= 1 
                    if (nums[left] + nums[middle] + nums[right]) < 0: 
                        break
                else: # cannot find with these left and rights
                    middle = n // 2
                    right -= 1
                    if right == middle:
                        break
            
            # if the sum is less than zero move the middle right
            else:
                if (middle + 1) != right:
                   middle += 1 
                   if (nums[left] + nums[middle] + nums[right]) > 0: 
                        break
                else: # cannot find with these left and rights
                    middle = n // 2
                    left += 1
                    if left == middle:
                        break

        return r




            

            

        



            

            
            
