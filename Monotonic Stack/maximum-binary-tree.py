# https://leetcode.com/problems/maximum-binary-tree/
# Difficulty: Medium
# Time:  O(n)
# Space: O(n)
# Approach: Monotonic Stack

from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        tree = {}
        for next_greater in nums:
            tree[next_greater] = TreeNode(next_greater)
            while stack and stack[-1] < next_greater:
                tree[next_greater].left = tree[stack.pop()]
            if stack:
                tree[stack[-1]].right = tree[next_greater]
            stack.append(next_greater)
        return tree[stack[0]]
