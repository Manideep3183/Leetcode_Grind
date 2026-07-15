class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        total_sum = sum(cardPoints)
        if n == k:
            return total_sum
        win_size = n - k
        curr_sum = sum(cardPoints[ : win_size])
        min_sum = curr_sum
        for i in range(win_size, n):
            curr_sum += cardPoints[i] - cardPoints[i - win_size]
            min_sum = min(curr_sum,min_sum)
        return total_sum - min_sum
        