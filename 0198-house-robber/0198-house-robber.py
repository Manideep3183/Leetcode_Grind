class Solution(object):
    def rob(self, nums):
        a = 0 
        b = nums[0]
        for i in range(1,len(nums)):
            r = max(a+nums[i],b)
            a = b
            b = r
        return b
        
        