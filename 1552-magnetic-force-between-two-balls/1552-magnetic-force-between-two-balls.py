class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        pos.sort()
        low, high = 1, pos[-1] - pos[0]
        ans = 0
        while low <= high:
            mid = (low + high) >> 1
            if self.isokay(mid,m,pos):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
    def isokay(self,mid,m,pos):
        last = pos[0]
        count = 1
        for i in range(len(pos)):
            if abs(pos[i] - last) >= mid:
                count += 1
                last = pos[i]
        return count >= m
    