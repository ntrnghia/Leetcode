# https://leetcode.com/problems/sum-of-subarray-ranges/
# Difficulty: Medium (Should be Hard)
# Time:  O(n)
# Space: O(n)
# Approach: Monotonic Stack
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0
        stack = []
        for next_larger in range(n+1):
            while stack and (next_larger == n or nums[stack[-1]] < nums[next_larger]):
                i = stack.pop()
                prev_larger = stack[-1] if stack else -1
                s += nums[i] * (i - prev_larger) * (next_larger - i)
            stack.append(next_larger)
        stack = []
        for next_smaller in range(n+1):
            while stack and (next_smaller == n or nums[stack[-1]] > nums[next_smaller]):
                i = stack.pop()
                prev_smaller = stack[-1] if stack else -1
                s -= nums[i] * (i - prev_smaller) * (next_smaller - i)
            stack.append(next_smaller)
        return s
