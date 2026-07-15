class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        def atmost(goal):
            if goal < 0:
                return 0
            l = 0
            count = 0
            sum = 0
            for r in range(len(nums)):
                sum += nums[r]
                while sum > goal:
                    sum -= nums[l]
                    l += 1
                count += (r-l+1)
            return count
        return atmost(goal) - atmost(goal-1)

                


        
        