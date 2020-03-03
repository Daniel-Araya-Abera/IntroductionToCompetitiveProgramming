class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        first = second = -1
        maxDistance = -1
        startOnly = True    
        for index in range(len(seats)):
            if seats[index] == 1:
                if first == -1:
                    first = index
                    if startOnly:
                        startOnly = False
                        if abs(first - 0) > maxDistance :
                            maxDistance = abs(first - 0)
                    
                if first != -1 and second == -1 and index != first:
                    second = index
                    optimalDistance = (first + second) // 2
                    dist1 = abs(optimalDistance - first)
                    dist2 = abs(optimalDistance - second)
                    possibleDistance = minDistance = min(dist1,dist2)
        
                    if possibleDistance > maxDistance:
                        maxDistance = possibleDistance
                    first = second
                    second = -1
        
        if first != len(seats) - 1:
            end = len(seats) - 1
            x = abs(first - end)
            if x > maxDistance:
                maxDistance = x
            
        return maxDistance
    
    