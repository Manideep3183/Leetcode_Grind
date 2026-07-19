class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def atMostK(dist_count):
            hash_map = {}
            left = 0
            total = 0
            for r in range(len(nums)):
                if hash_map.get(nums[r], 0) == 0:
                    dist_count -= 1
                hash_map[nums[r]] = hash_map.get(nums[r],0) + 1
                while dist_count < 0:
                    hash_map[nums[left]] -= 1
                    if hash_map[nums[left]] == 0:
                        dist_count += 1
                    left += 1
                total += r - left
            return total
        return atMostK(k) - atMostK(k-1)
