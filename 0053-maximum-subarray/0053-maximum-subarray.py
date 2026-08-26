class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        max_sum = nums[0]
        for right in nums:
            curr += right
            max_sum = max(max_sum, curr)
            if curr < 0:
                curr = 0
        return max_sum