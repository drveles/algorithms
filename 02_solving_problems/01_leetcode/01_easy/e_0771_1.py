class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew_set = set(jewels)

        return sum(1 for stone in stones if stone in jew_set)
