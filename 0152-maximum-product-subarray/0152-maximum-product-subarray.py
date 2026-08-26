class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = ans = nums[0]
        for num in nums[1:]:
            candidates = (num, max_prod * num, min_prod * num)
            max_prod, min_prod = max(candidates), min(candidates)
            ans = max(ans,max_prod)
        return ans