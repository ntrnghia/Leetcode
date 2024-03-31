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
        for next_greater in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[next_greater]:
                m[nums2[stack.pop()]] = nums2[next_greater]
            stack.append(next_greater)
        return [m[num] if num in m else -1 for num in nums1]
