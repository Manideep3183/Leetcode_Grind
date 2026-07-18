import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_val = nums[0]
        max_val = nums[0]
        for i in range(len(nums)):
            if min_val > nums[i]:
                min_val = nums[i]
            if max_val < nums[i]:
                max_val = nums[i]
        return math.gcd(min_val,max_val)
        