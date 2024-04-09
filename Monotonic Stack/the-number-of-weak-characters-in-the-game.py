# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
# Difficulty: Medium
# Time:  O(nlogn)
# Space: O(n)

from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))

        max_defense = 0
        weak_characters = 0

        # Iterate over the properties
        for _, defense in properties:
            # If the current defense is less than the max defense seen so far,
            # it means this character is weak
            if defense < max_defense:
                weak_characters += 1
            else:
                # Update max_defense with the current character's defense
                # because this defense is not weak at its position
                max_defense = defense

        return weak_characters
