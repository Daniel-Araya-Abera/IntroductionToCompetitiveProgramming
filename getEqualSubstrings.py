class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        count = i = 0
        limit = 0
        viableEnd = min(len(s), len(t))
        # print("viable End is ", viableEnd)
        for i in range(viableEnd):
            if s[i] == t[i]:
                count += 1
                # print("at index ", i, " they r equal")
            else:
                first = ord(s[i]) - ord('a')
                second = ord(t[i]) - ord('a')
                print("for INDEX I = ", i, ", first is ", first, " and second is ", second)
                diff = abs(first - second)
                if diff + limit <= maxCost :
                    limit += diff
                    count += 1
                else:
                    return count
        return count