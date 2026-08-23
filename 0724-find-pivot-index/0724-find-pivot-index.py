class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            total -= nums[i]
            if total == left_sum:
                return i
            left_sum += nums[i]
        return -1

        