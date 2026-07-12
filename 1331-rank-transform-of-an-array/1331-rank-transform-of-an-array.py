class Solution(object):
    def arrayRankTransform(self, arr):
        unq_sorted = sorted(list(set(arr)))
        rank_map = {}
        for index, val in enumerate(unq_sorted):
            rank_map[val] = index+1
        return [rank_map[x] for x in arr]
        