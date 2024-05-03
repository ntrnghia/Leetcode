# https://leetcode.com/problems/longest-well-performing-interval/
# Difficulty: Medium
# Time:  O(n)
# Space: O(n)

from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        first_index_have_sum = {}
        cur_sum = 0
        res = 0
        for i, h in enumerate(hours):
            cur_sum += (1 if h > 8 else -1)
            if cur_sum > 0:
                res = i + 1
            else:
                if cur_sum not in first_index_have_sum:
                    first_index_have_sum[cur_sum] = i
                if cur_sum - 1 in first_index_have_sum:
                    res = max(res, i - first_index_have_sum[cur_sum - 1])
        return res
