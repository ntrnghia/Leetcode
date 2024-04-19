# https://leetcode.com/problems/beautiful-towers-i/
# Difficulty: Medium
# Time:  O(n)
# Space: O(n)

from typing import List


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        stack = []  # (val, span)
        left_sum = []
        cum = 0
        for i in range(n):
            span = 1
            while stack and stack[-1][0] > maxHeights[i]:
                val, s = stack.pop()
                cum -= val * s
                span += s
            stack.append((maxHeights[i], span))
            cum += maxHeights[i] * span
            left_sum.append(cum)

        stack = []  # (val, span)
        cum = 0
        res = 0
        for i in range(n-1, -1, -1):
            span = 1
            while stack and stack[-1][0] > maxHeights[i]:
                val, s = stack.pop()
                cum -= val * s
                span += s
            stack.append((maxHeights[i], span))
            cum += maxHeights[i] * span
            res = max(res, left_sum[i] + cum - maxHeights[i])
        return res
