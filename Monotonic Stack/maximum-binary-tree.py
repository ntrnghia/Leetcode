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
        top = None
        for num in nums:
            tree[num] = TreeNode(num)
            while stack and num > stack[-1]:
                top = stack.pop()
                tree[num].left = tree[top]
            if stack:
                tree[stack[-1]].right = tree[num]
            stack.append(num)
        return tree[stack[0]]
