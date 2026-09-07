from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        counts = Counter(nums)
        threshold = len(nums) // 3
        
        return [num for num, count in counts.items() if count > threshold]