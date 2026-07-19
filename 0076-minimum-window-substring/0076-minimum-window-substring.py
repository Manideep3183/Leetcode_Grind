from collections import Counter
class Solution():
    def minWindow(self,s,t):
        if not t or not s:
            return ""
        freq = Counter(t)
        min_len = float('inf')
        left = 0
        ans = ''
        count = len(t)
        for right in range(len(s)):
            if freq[s[right]] > 0:
                count -= 1
            freq[s[right]] -= 1

            while count == 0:
                if min_len > right-left+1:
                    ans = s[left :  right+1]
                    min_len = right-left+1
                
                freq[s[left]] += 1
                if freq[s[left]] > 0:
                    count += 1
                left += 1
        return ans