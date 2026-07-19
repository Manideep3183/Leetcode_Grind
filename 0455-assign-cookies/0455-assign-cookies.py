class Solution(object):
    def findContentChildren(self, g, s):
        n, m = len(g), len(s)
        s.sort()
        g.sort()
        l, r = 0, 0
        while l < m:
            if r == n:
                break
            if g[r] <= s[l]:
                r += 1
            l += 1
        return r
        