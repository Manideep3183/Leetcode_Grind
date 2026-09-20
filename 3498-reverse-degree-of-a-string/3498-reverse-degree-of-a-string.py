class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            total += (123 - ord(s[i])) * (i + 1)
        return total
