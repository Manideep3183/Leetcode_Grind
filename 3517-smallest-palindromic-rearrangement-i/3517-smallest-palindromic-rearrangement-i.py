class Solution(object):
    def smallestPalindrome(self, s):
        n = len(s)
        half_len = n // 2
        
        first_half = "".join(sorted(s[:half_len]))
        mid = s[half_len] if n % 2 != 0 else ""
        
        return first_half + mid + first_half[::-1]