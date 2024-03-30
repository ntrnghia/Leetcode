# https://leetcode.com/problems/sum-of-subarray-ranges/
# Difficulty: Medium (Should be Hard)
# Time:  O(n)
# Space: O(n)
# Approach: Monotonic Stack
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        left_min = [len(nums)-idx for idx in range(len(nums))]
        right_min = [1]*len(nums)
        stack = []
        for idx, num in enumerate(nums):
            while stack and num < nums[stack[-1]]:
                top = stack.pop()
                left_min[top] = idx - top
                right_min[idx] += right_min[top]
            stack.append(idx)
        left_max = [len(nums)-idx for idx in range(len(nums))]
        right_max = [1]*len(nums)
        stack = []
        for idx, num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                top = stack.pop()
                left_max[top] = idx - top
                right_max[idx] += right_max[top]
            stack.append(idx)
        return sum([nums[idx]*(left_max[idx]*right_max[idx]-left_min[idx]*right_min[idx]) for idx in range(len(nums))])
