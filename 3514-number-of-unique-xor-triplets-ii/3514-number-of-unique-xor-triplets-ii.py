class Solution:
    def uniqueXorTriplets(self, nums):
        unique_nums = set(nums)
        
     
        pair_xors = set()
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                pair_xors.add(nums[i] ^ nums[j])
        
       
        triplet_xors = set()
        for px in pair_xors:
            for x in unique_nums:
                triplet_xors.add(px ^ x)
                
        return len(triplet_xors)