class Solution:
    def checkDivisibility(self, n: int) -> bool:
        dsum = 0
        dprod = 1
        temp = n
        while n > 0:
            d = n % 10
            dsum += d
            dprod *= d
            n = n // 10
        return temp % (dsum + dprod) == 0