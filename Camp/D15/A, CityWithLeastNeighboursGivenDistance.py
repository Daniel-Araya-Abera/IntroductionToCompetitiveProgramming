class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        shortestMap = []
        for i in range(n):
            shortestMap.append([])
        for i in range(n):
            for j in range(n):
                shortestMap[i].append(float('inf'))
        
        for i in range(n):
            shortestMap[i][i] = 0
        for i in range(len(edges)):
            start = edges[i][0]
            end = edges[i][1]
            distance = edges[i][2]
            shortestMap[start][end] = shortestMap[end][start] = distance
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    calculatedDistance = shortestMap[i][k] + shortestMap[k][j]
                    if calculatedDistance < shortestMap[i][j]:
                        shortestMap[i][j] = calculatedDistance
        resultCity = None
        maxCount = n - 1 ## should initialize this to maxx value
        for i in range(n):
            count = 0
            for j in range(n):
                if shortestMap[i][j] <= distanceThreshold and i != j:
                    count += 1
            if count <= maxCount:
                maxCount = count
                resultCity = i
        return resultCity