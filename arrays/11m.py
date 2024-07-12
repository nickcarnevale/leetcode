# https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # what are we looking for:
        # max area if each num in array is a distance upwardsm (height). 
        # the width would come from the difference in index.

        # initial thought, search array from both sides calculating max area and work way inwards
        # keep a pointer on the taller of the two heights

        n = len(height)
        l = 0
        r = n - 1
        max = 0

        while True: 

            leftHeight = height[l]
            rightHeight = height[r]
            smallerHeight = min(leftHeight, rightHeight)
            width = r - l
            area = width * smallerHeight

            if area > max:
                max = area
            
            if smallerHeight == leftHeight:
                l += 1
            else:
                r -= 1

            if l == r:
                break

        return max
            

            





        



