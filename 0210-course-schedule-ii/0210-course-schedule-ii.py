from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = [0] * numCourses

        graph = defaultdict(list)

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        queue = deque()
        
        for c in range(numCourses):
            if indegree[c] == 0:
                queue.append(c)

        topo = []

        while queue:
            v = queue.popleft()
            topo.append(v)
            for neigh in graph[v]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        return topo if len(topo) == numCourses else []
                
                




        