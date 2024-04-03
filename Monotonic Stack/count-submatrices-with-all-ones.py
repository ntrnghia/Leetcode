# https://leetcode.com/problems/count-submatrices-with-all-ones/
# Difficulty: Medium
# Time:  O(m * n)
# Space: O(n)

from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        res = 0
        his = []
        for i, row in enumerate(mat):
            cur = []
            stack = []
            cnt = 0
            for j, cell in enumerate(row):
                cum = 0
                if cell == 1:
                    cum = his[i-1][j] + 1 if i else 1
                cur.append(cum)
                while stack and cur[stack[-1]] > cum:
                    jj = stack.pop()
                    cnt -= (jj-(stack[-1] if stack else -1))*(cur[jj]-cum)
                stack.append(j)
                cnt += cum
                res += cnt
            his.append(cur)
        return res
