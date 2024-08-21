# https://leetcode.com/problems/minimum-cost-for-tickets/description/

class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """


        n = len(days)
        dp = {}

        def dfs(i):
            if i >= n:
                return 0

            if i in dp:
                return dp[i]

            # 1-day pass
            option1 = costs[0] + dfs(i + 1)

            # 7-day pass
            j = i
            while j < n and days[j] < days[i] + 7:
                j += 1
            option2 = costs[1] + dfs(j)

            # 30-day pass
            k = i
            while k < n and days[k] < days[i] + 30:
                k += 1
            option3 = costs[2] + dfs(k)

            dp[i] = min(option1, option2, option3)
            return dp[i]

        return dfs(0)


              