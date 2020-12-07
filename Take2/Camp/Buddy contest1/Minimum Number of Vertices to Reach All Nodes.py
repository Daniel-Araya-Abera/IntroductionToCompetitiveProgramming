class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        visited = set()
        for i in range(len(edges)):
            visited.add(edges[i][1])
        
        res = []
        for i in range(n):
            if i not in visited:
                res.append(i)
        
        return res