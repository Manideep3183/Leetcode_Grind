class Solution(object):
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        total = m * n
        k = k % total
        res = [[0] * n for _ in range(m)]
        for idx in range(total):
            new_idx = (idx + k) % total  
            org_row, org_col = idx // n, idx % n
            new_row, new_col = new_idx // n, new_idx % n
            res[new_row][new_col] = grid[org_row][org_col]     
        return res