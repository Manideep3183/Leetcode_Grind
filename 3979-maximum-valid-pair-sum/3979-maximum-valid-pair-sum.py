class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        max_val = -float('inf')
        max_left = -float('inf')
        for j in range(k, len(nums)):
            max_left = max(max_left, nums[j-k])
            max_val = max(max_val, max_left + nums[j])
        return max_val    
            
