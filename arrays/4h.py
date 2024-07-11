# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # join the two arrays
        # cases, len(nums1) + len(nums1) can be even or odd

        # if odd, median is arr[len(nums)/2]
        # if even, median is (arr[len(nums)/2] + arr[len(nums)/2-1]) / 2

        # since arrays are sorted, combining is as simple as iterating through them 
        # this would be O(n) time however

        #lets try it. 

        num=nums1+nums2
        num.sort()
        l=len(num)
        if l%2==1:
            return num[l/2]
        else:
            return (num[l//2-1]+num[l//2])/2.0
        




        