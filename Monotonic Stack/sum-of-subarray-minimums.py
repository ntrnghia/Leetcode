# https://leetcode.com/problems/sum-of-subarray-minimums/
# Difficulty: Medium
# Time:  O(n)
# Space: O(n)
# Approach: Monotonic Stack
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        dif_index = [len(arr)-idx for idx in range(len(arr))]
        mul_factor = [1]*len(arr)
        stack = []
        for idx, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                top = stack.pop()
                dif_index[top] = idx - top
                mul_factor[idx] += mul_factor[top]
            stack.append(idx)
        s = 0
        for idx in range(len(arr)):
            s = (s + dif_index[idx]*mul_factor[idx]*arr[idx]) % (10**9+7)
        return s


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        right = [len(arr)]*len(arr)
        stack = []
        for idx, num in enumerate(arr):
            while stack and num <= arr[stack[-1]]:
                right[stack.pop()] = idx
            stack.append(idx)
        left = [-1]*len(arr)
        stack = []
        for idx in range(len(arr)-1, -1, -1):
            while stack and arr[idx] < arr[stack[-1]]:
                left[stack.pop()] = idx
            stack.append(idx)
        s = 0
        for idx, num in enumerate(arr):
            s = (s + num * (right[idx]-idx) * (idx-left[idx])) % (10**9+7)
        return s
