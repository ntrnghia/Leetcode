# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
# Difficulty: Medium
# Time:  O(n)
# Space: O(n)

from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        right = n - 1
        while left + 1 < n and arr[left] <= arr[left+1]:
            left += 1
        if left == n - 1:
            return 0
        while right > 0 and arr[right] >= arr[right-1]:
            right -= 1
        res = min(n - 1 - left, right)
        i = 0
        j = right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                res = min(res, j - i - 1)
                i += 1
            else:
                j += 1
        return res
