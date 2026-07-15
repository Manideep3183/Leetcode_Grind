class Solution(object):
    def findmax(self,nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        a = 0
        b = nums[0]
        for num in nums[1:]:
            r = max(a + num,b)
            a = b
            b = r
        return b
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.findmax(nums[1:]),self.findmax(nums[:-1]))
    
    
        
        
        