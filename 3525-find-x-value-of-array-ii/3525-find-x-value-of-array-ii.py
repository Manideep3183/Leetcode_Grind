class SegmentTree:
    def __init__(self, data, k):
        self.n = len(data)
        self.k = k
        self.tree_prod = [1] * (4 * self.n)
        self.tree_count = [[0] * k for _ in range(4 * self.n)]
        self.build(data, 1, 0, self.n - 1)

    def merge(self, left_prod, left_count, right_prod, right_count):
        prod = (left_prod * right_prod) % self.k
        count = list(left_count)
        for r in range(self.k):
            c = right_count[r]
            if c:
                count[(left_prod * r) % self.k] += c
        return prod, count

    def build(self, data, node, l, r):
        if l == r:
            val = data[l] % self.k
            self.tree_prod[node] = val
            self.tree_count[node][val] = 1
            return
        mid = (l + r) // 2
        self.build(data, 2 * node, l, mid)
        self.build(data, 2 * node + 1, mid + 1, r)
        self.tree_prod[node], self.tree_count[node] = self.merge(
            self.tree_prod[2 * node], self.tree_count[2 * node],
            self.tree_prod[2 * node + 1], self.tree_count[2 * node + 1]
        )

    def update(self, node, l, r, idx, val):
        if l == r:
            v = val % self.k
            self.tree_prod[node] = v
            self.tree_count[node] = [0] * self.k
            self.tree_count[node][v] = 1
            return
        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node, l, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, val)
        self.tree_prod[node], self.tree_count[node] = self.merge(
            self.tree_prod[2 * node], self.tree_count[2 * node],
            self.tree_prod[2 * node + 1], self.tree_count[2 * node + 1]
        )

    def query(self, node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.tree_prod[node], self.tree_count[node]
        mid = (l + r) // 2
        if qr <= mid:
            return self.query(2 * node, l, mid, ql, qr)
        if ql > mid:
            return self.query(2 * node + 1, mid + 1, r, ql, qr)
        
        left_prod, left_count = self.query(2 * node, l, mid, ql, qr)
        right_prod, right_count = self.query(2 * node + 1, mid + 1, r, ql, qr)
        return self.merge(left_prod, left_count, right_prod, right_count)


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = SegmentTree(nums, k)
        ans = []
        for idx, val, start, x in queries:
            tree.update(1, 0, n - 1, idx, val)
            _, counts = tree.query(1, 0, n - 1, start, n - 1)
            ans.append(counts[x])
        return ans