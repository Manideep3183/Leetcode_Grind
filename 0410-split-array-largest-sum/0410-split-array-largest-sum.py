class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def helper(mid):
            count = 1
            curr_sum = 0
            for num in nums:
                if curr_sum + num > mid:
                    count += 1
                    curr_sum = 0
                curr_sum += num
            return count
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low+high) >> 1
            count = helper(mid)
            if count > k:
                low = mid + 1
            else:
                high = mid - 1
        return low


        