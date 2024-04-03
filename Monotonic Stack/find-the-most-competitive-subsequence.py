# https://leetcode.com/problems/find-the-most-competitive-subsequence/
# Difficulty: Medium
# Time:  O(n)
# Space: O(k)
from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []
        for next_smaller in range(n):
            while stack and stack[-1] > nums[next_smaller] and n - 1 - next_smaller >= k - len(stack):
                stack.pop()
            if len(stack) < k:
                stack.append(nums[next_smaller])
        return stack
