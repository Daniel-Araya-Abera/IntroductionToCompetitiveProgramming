# https://leetcode.com/problems/longest-palindromic-subsequence/
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memoizer = {}
        start = 0
        end = len(s) - 1
        result = self.helper(s, start, end, memoizer)
        return result
        
    def helper(self, s, start, end, memoizer):
        
        if start > end:
            return 0
        if start == end:
            return 1
        
        if (start,end) in memoizer:
            return memoizer[(start,end)]
        
        if s[start] == s[end]:
            result = self.helper(s,start + 1, end - 1, memoizer) + 2
            memoizer[(start,end)] = result
            return result
        first =  self.helper(s, start + 1, end, memoizer)
        second = self.helper(s, start, end - 1, memoizer)
        result = max(first, second)
        memoizer[(start,end)] = result
        return result