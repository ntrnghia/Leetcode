# https://leetcode.com/problems/next-greater-element-i/
# Difficulty: Easy
# Time:  O(n)
# Space: O(n)
# Approach: Monotonic Stack

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        m = {}
        for num in reversed(nums2):
            while stack and num > stack[-1]:
                stack.pop()
            if stack:
                m[num] = stack[-1]
            else:
                m[num] = -1
            stack.append(num)
        return [m[num] for num in nums1]
