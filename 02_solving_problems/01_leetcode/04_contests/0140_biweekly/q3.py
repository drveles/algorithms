# You are given two strings wordi and word2. < 00:28:42 3 <>Code Python3 Attempted 1 class Solution: 2 3 5 A string x is called almost equal to y if you can change at most one character in x to make it identical to y. 6 7 A sequence of indices seg is called valid if: 9 The indices are sorted in ascending order. 10 11 Concatenating the characters at these indices in word1 in the same order results in a string that is almost equal to word2. 12 13 Return an array of size word2. length representing the lexicographically smallest valid sequence of indices. If no such sequence of indices exists, return an empty array. 14 15 Note that the answer must represent the lexicographically smallest array, not the corresponding string formed by those indices. 16 17 18


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        index_map = {}
        result = []

        for i, char in enumerate(word2):
            if char not in index_map:
                index_map[char] = []
            index_map[char].append(i)

        for x, char in enumerate(word1):
            if char in index_map:
                for y in index_map[char]:
                    result.append(x)

        result.sort()

        return result if result else []


# WA
