# https://leetcode.com/problems/next-greater-node-in-linked-list/
# Difficulty: Medium
# Time:  O(n)
# Space: O(n)
# Approach: Monotonic Stack
from typing import List, Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        stack = []
        ans = [0]*len(nums)
        for next_greater in range(len(nums)):
            while stack and nums[stack[-1]] < nums[next_greater]:
                ans[stack.pop()] = nums[next_greater]
            stack.append(next_greater)
        return ans
