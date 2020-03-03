class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        frequency = [0] * len(shifts)
        summ = sum(shifts)
        frequency[0] = summ
        for i in range(1, len(frequency)):
            frequency[i] = frequency[i - 1] - shifts[i - 1]
        
        result = "" ## better use join function with array of strings maybe
        for i in range(len(S)):
            result += self.shiftSingleLetter( S[i], frequency[i] )
        return result
        
    def shiftSingleLetter(self, singleLetter: str, shift: int) -> str:
        original = ord(singleLetter) - ord('a')
        final = (original + shift) % 26 + ord('a')
        final = chr(final)
        return final
        
