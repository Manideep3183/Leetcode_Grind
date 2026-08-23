class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(ind,path,target):
            if ind == len(candidates):
                if target == 0:
                    res.append(path[:])
                return
            elif candidates[ind] <= target:
                path.append(candidates[ind])
                backtrack(ind, path, target - candidates[ind])
                path.pop()
            backtrack(ind + 1, path, target)
        res = []
        backtrack(0, [], target)
        return res