# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
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
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        stack = []
        m = {}
        for num in preorder:
            m[num] = TreeNode(num)
            top = None
            while stack and num > stack[-1]:
                top = stack.pop()
            if top:
                m[top].right = m[num]
            elif stack:
                m[stack[-1]].left = m[num]
            stack.append(num)
        return m[preorder[0]]
