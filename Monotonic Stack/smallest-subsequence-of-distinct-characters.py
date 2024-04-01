# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# Difficulty: Medium
# Time:  O(n)
# Space: O(n)
# Approach: Monotonic Stack

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        stack = []
        occur = set()
        for ch in s:
            count[ch] -= 1
            if ch not in occur:
                while stack and count[stack[-1]] > 0 and stack[-1] >= ch:
                    occur.remove(stack.pop())
                stack.append(ch)
                occur.add(ch)
        return ''.join(stack)
