class Solution:
    def maxPossibleScore(self, start: list[int], d: int) -> int:
        start.sort()
        n = len(start)

        def can_achieve(score: int) -> bool:
            prev = start[0]
            for i in range(1, n):
                
                next_val = max(start[i], prev + score)
                if next_val > start[i] + d:
                    return False
                prev = next_val
            return True

     
        low = 0
        high = (start[-1] + d - start[0])
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if can_achieve(mid):
                ans = mid
                low = mid + 1 
            else:
                high = mid - 1  

        return ans