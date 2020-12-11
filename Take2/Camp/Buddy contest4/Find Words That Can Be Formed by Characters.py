"""
let n = len(words), m = len(chars), o = len(max(words))
time-complexity -> O(nom)
"""
from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = Counter(chars)
        total_len = 0
        
        for word in words:
            found = True
            for char in word:
                if char not in freq or freq[char] == 0:
                    found = False
                    break
                freq[char] -= 1
            if found:
                total_len += len(word)
            freq = Counter(chars)
        
        return total_len
        