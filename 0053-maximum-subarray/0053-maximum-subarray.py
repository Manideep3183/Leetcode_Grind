class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        max_sum = 0
        for right in nums:
            curr += right
            if curr < 0:
                curr = 0
            max_sum = max(max_sum, curr)
        return max_sum