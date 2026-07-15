class Solution(object):
    def numberOfSubarrays(self, nums, k):
        def atmost(k):
            if k < 0:
                return 0
            l = 0
            odd_count = 0
            subarrays = 0
            for r in range(len(nums)):
                if nums[r] % 2:
                    odd_count += 1
                while odd_count > k:
                    if nums[l] % 2:
                        odd_count -= 1
                    l += 1
                subarrays += (r-l+1)
            return subarrays
        return atmost(k) - atmost(k-1)


            
                