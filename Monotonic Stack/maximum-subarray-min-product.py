# https://leetcode.com/problems/maximum-subarray-min-product/
# Difficulty: Medium
# Time:  O(n)
# Space: O(n)

from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        csum = 0  # cumulative sum
        stack = []  # (val, csum)
        res = 0  # result
        nums.append(0)  # sentinel
        for num in nums:  # monotonic stack
            while stack and stack[-1][0] > num:  # pop
                vmin, _ = stack.pop()  # val, csum
                # update result
                res = max(res, vmin * (csum - (stack[-1][1] if stack else 0)))
            csum += num  # update cumulative sum
            stack.append((num, csum))  # push
        return res % (pow(10, 9)+7)  # return result modulo 10^9+7
