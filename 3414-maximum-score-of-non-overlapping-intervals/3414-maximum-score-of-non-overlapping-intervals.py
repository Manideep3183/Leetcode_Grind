from bisect import bisect_left
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = sorted((r, l, w, i) for i, (l, r, w) in enumerate(intervals))
        r_vals = [x[0] for x in arr]
        
        dp = [[(0, []) for _ in range(n + 1)] for _ in range(5)]
        
        for i in range(n):
            r_i, l_i, w_i, orig_idx = arr[i]
            prev_idx = bisect_left(r_vals, l_i)
            
            for k in range(1, 5):
                best_w, best_ids = dp[k][i]
                
                prev_w, prev_ids = dp[k - 1][prev_idx]
                cand_w = prev_w + w_i
                cand_ids = sorted(prev_ids + [orig_idx])
                
                if cand_w > best_w:
                    best_w, best_ids = cand_w, cand_ids
                elif cand_w == best_w and cand_ids < best_ids:
                    best_ids = cand_ids
                
                dp[k][i + 1] = (best_w, best_ids)
                
        return dp[4][n][1]