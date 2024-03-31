# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/
# Difficulty: Easy
# Time:  O(n)
# Space: O(n)
# Approach: Monotonic Stack

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for next_smaller in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[next_smaller]:
                prices[stack.pop()] -= prices[next_smaller]
            stack.append(next_smaller)
        return prices
