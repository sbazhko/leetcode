# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        currMin = 0
        i = 0
        while i < len(prices):
            profit = max(profit, prices[i] - prices[currMin])
            if prices[i] < prices[currMin]:
                currMin = i
            i += 1

        return profit


s = Solution()

assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert s.maxProfit([7, 6, 5]) == 0
assert s.maxProfit([7]) == 0
