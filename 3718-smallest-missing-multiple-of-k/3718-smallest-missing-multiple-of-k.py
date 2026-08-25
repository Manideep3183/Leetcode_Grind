class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)
        curr = k
        while curr in nums_set:
            curr += k
        return curr

            
            
         