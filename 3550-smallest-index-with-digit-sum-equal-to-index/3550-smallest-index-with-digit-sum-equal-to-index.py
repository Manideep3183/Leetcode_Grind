class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i,num in enumerate(nums):
            d_sum = 0
            
            while num > 0:
                d_sum += num % 10
                num = num // 10
            if i == d_sum:
                return i
                break
        return -1
            
        