class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            total += (26 - (ord(s[i]) - ord('a'))) * (i + 1)
        return total
