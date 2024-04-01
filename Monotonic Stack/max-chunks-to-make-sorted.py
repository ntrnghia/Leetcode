# https://leetcode.com/problems/max-chunks-to-make-sorted/
# Difficulty: Medium
# Time:  O(n)
# Space: O(1)
# Approach: Monotonic Stack

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxi = -1
        res = 0
        for i in range(len(arr)):
            maxi = max(arr[i], maxi)
            if maxi == i:
                res += 1
        return res


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for num in arr:
            if stack and num < stack[-1]:
                top = stack.pop()
                while stack and num < stack[-1]:
                    stack.pop()
                stack.append(top)
            else:
                stack.append(num)
        return len(stack)
