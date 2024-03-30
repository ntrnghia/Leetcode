# https://leetcode.com/problems/remove-nodes-from-linked-list
# Difficulty: Medium
# Time:  O(n)
# Space: O(n)
# Approach: Monotonic Stack
from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head
        while cur:
            while stack and cur.val > stack[-1].val:
                stack.pop()
            stack.append(cur)
            cur = cur.next
        for idx in range(len(stack)-1):
            stack[idx].next = stack[idx+1]
        return stack[0]
