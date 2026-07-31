from collections import Counter

class Solution(object):
    def minimumPushes(self, word):
        counts = Counter(word)
        freqs = sorted(counts.values(), reverse=True)  
        total_pushes = 0
        for i, freq in enumerate(freqs):
            pushes_per_char = (i // 8) + 1
            total_pushes += freq * pushes_per_char  
        return total_pushes