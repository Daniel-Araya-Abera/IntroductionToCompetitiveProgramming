class Solution:
    def lastSubstring(self, s: str) -> str:
        max_letter = 'a'
        maxx = ""
        
        for i, char in enumerate(s):
            max_letter = max(max_letter, char)
                    
        for i in range(len(s)):
            if s[i] == max_letter:
                if s[i:] > maxx:
                    maxx = s[i:]
        
        return maxx
        