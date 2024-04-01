# https://leetcode.com/problems/max-chunks-to-make-sorted-ii/
# Difficulty: Hard
# Time:  O(n)
# Space: O(n)
# Approach: Monotonic Stack

from typing import List


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
