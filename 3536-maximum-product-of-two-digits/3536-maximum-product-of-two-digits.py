class Solution(object):
    def maxProduct(self, n):
        res = []
        while n > 0:
            res.append(n % 10)
            n = n // 10
        res.sort()
        return res[-1] * res[-2]
        

        
        
        