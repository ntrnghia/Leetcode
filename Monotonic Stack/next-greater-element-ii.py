# https://leetcode.com/problems/next-greater-element-ii/description/
# Difficulty: Medium
# Time:  O(n)
# Space: O(n)
# Approach: Monotonic Stack
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        nums = nums + nums
        stack = []
        for idx in range(len(nums)):
            while stack and nums[idx] > nums[stack[-1]]:
                res[stack.pop()] = nums[idx]
            stack.append(idx % n)
        return res
