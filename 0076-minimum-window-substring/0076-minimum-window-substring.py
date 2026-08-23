from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t)>len(s):
            return ''
        count = len(t)
        freq = Counter(t)
        min_len = float('inf')
        l = 0
        ans = ''
        for r in range(len(s)):
            if freq[s[r]] > 0:
                count -= 1
            freq[s[r]] -= 1
            while count == 0:
                if min_len > r - l + 1:
                    ans = s[l:r+1]
                    min_len = r-l+1
                freq[s[l]] += 1
                if freq[s[l]] > 0:
                    count += 1
                l += 1
        return ans
