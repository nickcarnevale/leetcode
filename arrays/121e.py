# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        n = len(prices)

        left = 0
        right = 1

        while right < n:

            if prices[left] > prices[right]:
                left = right
                right += 1
            else:
                profit = max(profit, prices[right] - prices[left])
                right += 1

        return profit


        