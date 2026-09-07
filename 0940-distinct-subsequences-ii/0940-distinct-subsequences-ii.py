class Solution:
    def distinctSubseqII(self, s: str) -> int:

        MOD = 10**9 + 7
        ends_with = [0] * 26
        for char in s:
            idx = ord(char) - ord('a')
            new = (1 + sum(ends_with)) % MOD
            ends_with[idx] = new
        return sum(ends_with) % MOD

        