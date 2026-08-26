class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse = True)
        chosen = nums[:k]
        sum = 0
        for num in chosen:
            if mul <= 0:
                sum += num
            else:
                sum += num * mul
            mul -= 1
        return sum

