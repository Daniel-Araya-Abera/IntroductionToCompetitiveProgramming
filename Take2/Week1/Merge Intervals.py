# Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# Difficulty: Medium

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            print("res val ", res[-1][1])
            print("intervla ", intervals[i][0])
            if res[-1][1] >= intervals[i][0]:
                if res[-1][1] >= intervals[i][1]:
                    pass
                    # res[-1][1] = intervals[i][1]
                else:
                    res[-1][1] = intervals[i][1]
            else:
                res.append(intervals[i])
        return res