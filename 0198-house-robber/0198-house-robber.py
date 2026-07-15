class Solution(object):
    def rob(self, nums):
        if not nums:
            return nums
        if len(nums) == 1:
            return nums[0]
        a = nums[0]
        b = max(nums[0],nums[1])
        for i in range(2, len(nums)):
            r = max(a+nums[i],b)
            a = b
            b = r
        return b
        
        
        