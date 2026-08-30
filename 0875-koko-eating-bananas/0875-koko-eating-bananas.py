class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(mid):
            time = 0
            for pile in piles:
                time += (pile + mid -1) // mid
            return time
        low = 1
        high = max(piles)
        while low < high:
            mid = (low + high) >> 1
            time = helper(mid)
            if time > h:
                low = mid + 1
            else:
                high = mid 
        return low