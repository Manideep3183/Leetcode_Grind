class Solution(object):
    def subsets(self, nums):
        res = []
        n = len(nums)
        subsets = 1 << n
        for i in range(subsets):
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(nums[j])
            res.append(subset)
        return res
                

        