class Solution(object):
    def maxSubarraySumCircular(self, nums):
        max_sum=nums[0]
        curr_max=0
        min_sum=nums[0]
        curr_min=0
        total_sum=0
        #Kadanes for both MIN and MAX sum
        #MAX SUM = Total - MIN SUM
        for num in nums:
            curr_max=max(num,curr_max+num)
            max_sum=max(curr_max,max_sum)
            curr_min=min(num,curr_min+num)
            min_sum=min(curr_min,min_sum)
            total_sum+=num
        if total_sum==min_sum:
                return max_sum
        return max(max_sum,total_sum-min_sum)
        