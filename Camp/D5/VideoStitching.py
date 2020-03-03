class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        frequency = {}
        for singleClip in clips:
            if singleClip[0] not in frequency:
                frequency[singleClip[0]] = singleClip[1]
            else:
                if singleClip[1] > frequency[singleClip[0]] :
                    frequency[singleClip[0]] = singleClip[1]
        
        sortedKeys = sorted(frequency)
        keysSet = set(sorted(frequency))
        
        if sortedKeys[0] != 0:
            return -1
        if frequency[sortedKeys[0]] >= T:
            return 1
        result = []
        result.append( [sortedKeys[0], frequency[sortedKeys[0]]] )
        
        count = 1
        while True:
            if count >= len(sortedKeys):
                return -1
            requiredKey = -1
            maxxFound = -1
            for i in range(result[-1][0] + 1, result[-1][1] + 1):
                if i in frequency:
                    if frequency[i] > maxxFound:
                        maxxFound = frequency[i]
                        requiredKey = i
            if not( requiredKey == -1 and maxxFound == -1) :
                result.append(   [requiredKey, maxxFound]   )
                if maxxFound >= T:
                    break
            else:
                return -1
            count += 1       
        return len(result)