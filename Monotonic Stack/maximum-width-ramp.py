# https://leetcode.com/problems/maximum-width-ramp/
# Difficulty: Medium
# Time:  O(n)
# Space: O(n)
from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)
        ans = 0
        for i in reversed(range(len(nums))):
            while stack and nums[stack[-1]] <= nums[i]:
                ans = max(ans, i - stack.pop())
        return ans
