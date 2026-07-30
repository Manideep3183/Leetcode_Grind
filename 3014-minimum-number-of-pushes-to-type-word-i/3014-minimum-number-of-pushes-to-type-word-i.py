class Solution(object):
    def minimumPushes(self, word):
        n = len(word)
        pushes = 0
        
        # 1st group of 8 letters (1 push each)
        if n > 0:
            pushes += min(n, 8) * 1
        # 2nd group of 8 letters (2 pushes each)
        if n > 8:
            pushes += min(n - 8, 8) * 2
        # 3rd group of 8 letters (3 pushes each)
        if n > 16:
            pushes += min(n - 16, 8) * 3
        # 4th group of letters (4 pushes each)
        if n > 24:
            pushes += (n - 24) * 4
            
        return pushes