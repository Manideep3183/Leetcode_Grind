class Solution(object):
    def gcdSum(self, nums):
        def gcd(a,b):
            if b == 0:
                return abs(a)
            return gcd(b,a%b)
        prefix_gcd = [0]*len(nums)
        max_num = nums[0]
        for i in range(len(nums)):
            if nums[i] > max_num:
                max_num = nums[i]
            prefix_gcd[i] = gcd(nums[i],max_num)
        prefix_gcd.sort()
        l = 0
        r = len(prefix_gcd)-1
        sum_gcd = 0
        while l < r:
            sum_gcd += gcd(prefix_gcd[l],prefix_gcd[r])
            l += 1
            r -= 1
        return sum_gcd


        