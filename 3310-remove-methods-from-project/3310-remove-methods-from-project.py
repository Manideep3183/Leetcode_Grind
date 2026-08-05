from collections import deque
class Solution(object):
    def remainingMethods(self, n, k, invocations):
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)
        suspicious = [False] * n
        suspicious[k] = True
        queue = deque([k])  
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not suspicious[neighbor]:
                    suspicious[neighbor] = True
                    queue.append(neighbor)
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))
        return [i for i in range(n) if not suspicious[i]]