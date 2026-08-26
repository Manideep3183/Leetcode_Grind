class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l = 0
        ans = ''
        count = 0
        for r in range(len(s)):
            if s[r] == '1':
                count += 1
            while k == count:
                sub = s[l : r + 1]
                if not ans or len(sub) < len(ans) or (len(sub) == len(ans) and sub < ans):
                    ans = sub
                if s[l] == '1':
                    count -= 1
                l += 1      
        return ans



