# https://leetcode.com/problems/last-stone-weight/description/

import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        # heaps in python are default minheaps
        # max heap workaround is multing by -1

        # O(n)
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)
    
        # O(n)
        while len(stones)>1:
            
            first = -1 * heapq.heappop(stones)
            second = -1 * heapq.heappop(stones)

            if first > second:
                heapq.heappush(stones, (-1 * (first-second)))


        if len(stones)>0:
            return -stones[0]
        else:
            return 0
