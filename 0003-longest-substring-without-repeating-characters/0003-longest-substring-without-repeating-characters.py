class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        char_ind = {}
        for r in range(len(s)):
            if s[r] in char_ind and char_ind[s[r]] >= l:
                l = char_ind[s[r]] + 1
            char_ind[s[r]] = r
            max_len = max(max_len,r-l+1)
        return max_len
        