class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        
        
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}

        def dp(i: int, m: int) -> int:
            
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            if (i, m) in memo:
                return memo[(i, m)]
            
            max_stones = 0
            
            for x in range(1, 2 * m + 1):
               
                current_take = suffix_sum[i] - dp(i + x, max(m, x))
                max_stones = max(max_stones, current_take)
                
            memo[(i, m)] = max_stones
            return memo[(i, m)]

        return dp(0, 1)