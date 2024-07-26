# https://leetcode.com/problems/zigzag-conversion/description/

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1 or numRows >= s:
            return s

        index, direction = 0, 1
        arr = [[] for _ in range(numRows)]

        for char in s:
            arr[index].append(char)
            if index == 0:
                direction = 1
            elif index == numRows -1:
                direction = -1
            
            index += direction

        
        for i in range(numRows):
            arr[i] = ''.join(arr[i])
        
        return ''.join(arr)  
