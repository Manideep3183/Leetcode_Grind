class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(ind,path):
            if ind == len(nums):
                res.append(path[:])
                return
            path.append(nums[ind])
            backtrack(ind+1,path)
            path.pop()
            backtrack(ind+1,path)
        backtrack(0,[])
        return res