# https://leetcode.com/problems/gas-station/description/

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1

        tank = 0
        res = 0

        for i in range(len(gas)):
            tank += (gas[i] - cost[i])

            if tank < 0:
                tank = 0
                res = i+1

        return res
            
