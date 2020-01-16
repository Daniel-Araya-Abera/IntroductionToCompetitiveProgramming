class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        firstReal = eval(a.split("+")[0])
        secondReal = eval(b.split("+")[0])  
        
        firstComplex = a.split("+")[1]
        ## remove the i from the imaginary part at the end.
        firstComplex = eval(firstComplex[:len(firstComplex) - 1]) 
        secondComplex = b.split("+")[1]        
        secondComplex = eval( secondComplex[:len(secondComplex) - 1] )
        
        resultReal = firstReal * secondReal - firstComplex * secondComplex 
        resultComplex = firstReal * secondComplex + firstComplex * secondReal
        resultFinal = ""
        resultFinal = str(resultReal) + "+" + str(resultComplex) + "i"
        return resultFinal
        
# s = Solution()
# s.complexNumberMultiply("1+1i", "2+2i")
# s.complexNumberMultiply("4+3i", "-3-4i")
# s.complexNumberMultiply("4+3i", "-3+-4i")
# s.complexNumberMultiply("1+-1i", "1+-1i")
# s.complexNumberMultiply("1+0i", "1+0i")