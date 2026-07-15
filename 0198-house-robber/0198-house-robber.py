class Solution(object):
    def rob(self, nums):
        a = 0 
        b = 0
        for i in range(len(nums)):
            r = max(a+nums[i],b)
            a = b
            b = r
        return b
        
        
        