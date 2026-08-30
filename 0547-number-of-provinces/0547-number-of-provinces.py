class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set()
        n = len(isConnected)
        
        def dfs(city):
            for neigh in range(n):
                if isConnected[city][neigh] == 1 and neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh)
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                provinces += 1
        return provinces
            
