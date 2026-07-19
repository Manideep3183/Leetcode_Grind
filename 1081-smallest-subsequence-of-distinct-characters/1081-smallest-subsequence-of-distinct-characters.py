class Solution(object):
    def smallestSubsequence(self, s):
        last = {c : i for i, c in enumerate(s)}
        vis = set()
        st = []
        for i, c in enumerate(s):
            if c in vis:
                continue
            while st and st[-1] > c and last[st[-1]] > i:
                vis.remove(st.pop())
            vis.add(c)
            st.append(c)
        return ''.join(st)
        