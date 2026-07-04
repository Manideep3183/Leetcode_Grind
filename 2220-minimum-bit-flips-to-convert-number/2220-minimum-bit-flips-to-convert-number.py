class Solution(object):
    def minBitFlips(self, start, goal):
        ans = start ^ goal
        count = 0
        while ans != 0:
            ans = (ans & ans-1)
            count += 1
        return count
        
        