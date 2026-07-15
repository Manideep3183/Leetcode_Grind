class Solution(object):
    def numberOfSubstrings(self, s):
        l = 0 
        substrings = 0
        counts = {'a':0,'b':0,'c':0}
        for r in range(len(s)):
            counts[s[r]] += 1
            while counts['a']>0 and counts['b']>0 and counts['c']>0:
                substrings += len(s) - r
                counts[s[l]] -= 1
                l += 1
        return substrings
        
        