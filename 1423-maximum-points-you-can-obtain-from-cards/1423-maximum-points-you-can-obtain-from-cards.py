class Solution(object):
    def maxScore(self, cardPoints, k):
        if k == len(cardPoints):
            return sum(cardPoints)
        maxscore = -1
        curr_sum = sum(cardPoints[:k])
        for i in range(1,k+2):
            if curr_sum > maxscore:
                maxscore = curr_sum
            curr_sum += cardPoints[-i] - cardPoints[k-i]
        return maxscore
        