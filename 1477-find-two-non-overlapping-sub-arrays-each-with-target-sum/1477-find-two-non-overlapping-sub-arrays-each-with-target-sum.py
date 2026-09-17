class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        min_lens = [float('inf')] * (n + 1)
        res = float('inf')
        
        curr_sum = 0
        left = 0
        
        for right in range(n):
            curr_sum += arr[right]
            
            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1
                
            min_lens[right + 1] = min_lens[right]
            
            if curr_sum == target:
                length = right - left + 1
                if min_lens[left] != float('inf'):
                    res = min(res, length + min_lens[left])
                min_lens[right + 1] = min(min_lens[right + 1], length)
                
        return res if res != float('inf') else -1