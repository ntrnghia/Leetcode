# https://leetcode.com/problems/car-fleet/
# Difficulty: Medium
# Time:  O(nlogn)
# Space: O(n)

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        time = [(target-position[i])/speed[i] for i in range(n)]
        time_pos_sorted = sorted(zip(time, position), key=lambda x: x[1])
        stack = []
        for next_greater, _ in time_pos_sorted:
            while stack and stack[-1] <= next_greater:
                stack.pop()
            stack.append(next_greater)
        return len(stack)
