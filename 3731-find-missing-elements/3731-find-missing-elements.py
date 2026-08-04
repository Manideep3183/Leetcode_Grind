class Solution(object):
    def findMissingElements(self, nums):
        res = []
        min_val = min(nums)
        max_val = max(nums)
        for num in range(min_val,max_val+1):
            if num not in nums:
                res.append(num)
        return res
        
        