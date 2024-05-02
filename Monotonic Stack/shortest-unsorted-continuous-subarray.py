# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# Difficulty: Medium
# Time:  O(n)
# Space: O(1)

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left + 1 < n and nums[left] <= nums[left+1]:
            left += 1
        if left == n - 1:
            return 0
        while right > 0 and nums[right] >= nums[right-1]:
            right -= 1
        mi = min(nums[left+1:n])
        ma = max(nums[:right])
        while left >= 0 and nums[left] > mi:
            mi = min(mi, nums[left])
            left -= 1
        while right < n and nums[right] < ma:
            ma = max(ma, nums[right])
            right += 1
        return right - left - 1
