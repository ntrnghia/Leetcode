# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/description/
# Difficulty: Medium
# Time:  O(n)
# Space: O(n)
# Approach: Monotonic Stack
from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = []
        res = [[float('inf'), float('inf')] for _ in range(len(arr))]
        for idx, num in enumerate(arr):
            while stack and num > arr[stack[-1]]:
                res[stack.pop()][0] = num
            stack.append(idx)
        stack = []
        for idx in range(len(arr)-1, -1, -1):
            while stack and arr[idx] >= arr[stack[-1]]:
                res[stack.pop()][1] = arr[idx]
            stack.append(idx)
        return sum([arr[idx]*min(res[idx]) for idx in range(len(arr)) if res[idx] != [float('inf'), float('inf')]])


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = []
        s = 0
        for next_greater in arr:
            while stack and stack[-1] < next_greater:
                i = stack.pop()
                s += min(stack[-1] if stack else float('inf'), next_greater)*i
            stack.append(next_greater)
        while stack:
            i = stack.pop()
            s += stack[-1]*i if stack else 0
        return s
