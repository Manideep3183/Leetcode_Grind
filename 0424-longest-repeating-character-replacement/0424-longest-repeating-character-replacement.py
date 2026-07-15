class Solution(object):
    def characterReplacement(self, s, k):
        l = 0
        max_len = 0
        count = {}
        max_freq = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0)+1
            max_freq = max(max_freq, count[s[r]])
            win_size = r-l+1
            repls = win_size - max_freq
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1 
            max_len = max(max_len, r - l + 1)
        return max_len

            
        
        