class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n==1:
            return 1
        indegree = [0]*(n+1)
        outdegree = [0]*(n+1)
        for i in trust:
            for j in range (2):
                if j==0:
                    outdegree[i[0]]+=1
                else:
                    indegree[i[1]] +=1
        for i in range (n+1):
            if indegree[i]==n-1 and outdegree[i]==0:
                return i
        return -1

