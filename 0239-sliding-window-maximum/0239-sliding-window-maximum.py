from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        q = deque()
        res = []
        for i in range(len(nums)):
            if q and q[0] < i - k + 1:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res
