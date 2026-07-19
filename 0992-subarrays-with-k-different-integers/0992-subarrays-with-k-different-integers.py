class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def atMostK(k):
            hash_map = {}
            left = 0
            total = 0
            for r in range(len(nums)):
                hash_map[nums[r]] = hash_map.get(nums[r],0) + 1
                while len(hash_map) > k:
                    hash_map[nums[left]] -= 1
                    if hash_map[nums[left]] == 0:
                        del hash_map[nums[left]]
                    left += 1
                total += r - left + 1    
            return total
        return atMostK(k) - atMostK(k-1)
