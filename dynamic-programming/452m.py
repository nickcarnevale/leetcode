# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        points.sort()
        n = len(points)

        leftStart = points[0][0]
        leftEnd = points[0][1]
        right = 1
        rval = 1

        if n == 1:
            return 1 

        while right < n:
            start = points[right][0]
            end = points[right][1]

            if start >= leftStart and start <= leftEnd:
                if end < leftEnd:
                    leftEnd = end
            else:
                leftStart = start
                leftEnd = end
                rval += 1
                
            right += 1

        return rval






        