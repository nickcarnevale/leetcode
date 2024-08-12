# https://leetcode.com/problems/candy/description/

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        n = len(ratings)
        candy = [1] * n

        # checking right neighbor

        for j in range(1, n):
            i = j-1
            if ratings[i] < ratings[j]:
                # then we know candy needs to at index j needs to be greater than candy at index i
                if candy[i] >= candy[j]:
                    candy[j] = candy[i] + 1

        # pass through the array and check the left neighbors

        for j in range(n-2, -1, -1):
            i = j+1
            if ratings[i] < ratings[j]:
                # then we know candy needs to at index j needs to be greater than candy at index i
                if candy[i] >= candy[j]:
                    candy[j] = candy[i] + 1

        return sum(candy)