class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range (n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set([source])
        qu =[]
        qu.append(source)
        while(len(qu)>0):
            node = qu.pop(0)
            if node==destination:
                return True
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    qu.append(neighbor)
        return False
        