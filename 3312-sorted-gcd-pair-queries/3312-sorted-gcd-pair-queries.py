import math
from collections import Counter
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        counts = Counter(nums)
        
        multiples_count = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            for j in range(i, max_val + 1, i):
                multiples_count[i] += counts[j]
                
        gcd_pairs_count = [0] * (max_val + 1)
        for i in range(max_val, 0, -1):
            c = multiples_count[i]
            total_pairs = c * (c - 1) // 2
            
            for j in range(2 * i, max_val + 1, i):
                total_pairs -= gcd_pairs_count[j]
                
            gcd_pairs_count[i] = total_pairs
            
        prefix_sum = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sum[i] = prefix_sum[i - 1] + gcd_pairs_count[i]
            
        ans = []
        for q in queries:
            idx = bisect_right(prefix_sum, q)
            ans.append(idx)
            
        return ans