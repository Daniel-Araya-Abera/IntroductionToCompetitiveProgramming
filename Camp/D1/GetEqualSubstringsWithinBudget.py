class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        viableEnd = min(len(s), len(t))
        start = 0
        end = 1
        count = i = 0
        maxx = 0
        limit = 0
        for i in range(viableEnd):
            end = i + 1
            
            first = ord(s[i]) - ord('a')
            second = ord(t[i]) - ord('a')
            diff = abs(first - second)
            
            limit = limit + diff

            while limit > maxCost:      
                first_diff = abs( ord(s[start]) - ord(t[start])  )
                limit = limit - first_diff
                start += 1
                
            maxx = max(maxx, end - start)

        return maxx