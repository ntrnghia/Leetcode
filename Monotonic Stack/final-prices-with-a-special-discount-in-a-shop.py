# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/
# Difficulty: Easy
# Time:  O(n)
# Space: O(n)
# Approach: Monotonic Stack

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = []
        for price in reversed(prices):
            while stack and price < stack[-1]:
                stack.pop()
            if stack:
                res.append(price - stack[-1])
            else:
                res.append(price)
            stack.append(price)
        return reversed(res)
