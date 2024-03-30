# https://leetcode.com/problems/daily-temperatures/
# Difficulty: Medium
# Time:  O(n)
# Space: O(n)
# Approach: Monotonic Stack
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                top = stack.pop()
                res[top] = idx - top
            stack.append(idx)
        return res
