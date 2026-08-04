class Solution(object):
    def findMissingElements(self, nums):
        res = []
        vis_num = set(nums)
        min_val = min(nums)
        max_val = max(nums)
        next_num = min_val + 1
        while next_num < max_val:
            if next_num not in vis_num:
                res.append(next_num)
            next_num += 1
        return res
        
        