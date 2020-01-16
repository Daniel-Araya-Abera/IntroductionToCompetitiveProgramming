class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        tempA = a[1:]
        tempB = b[1:]
        print("temp A ", tempA)
        print("temp B ", tempB)
        negativeA = negativeB = False
        if "-" in tempA:
            negativeA = True
        if "-" in tempB:
            negativeB = True
        
        print("NEGATIVE A ", negativeA)
        print("NEGATIVE B", negativeB)
        
        if not negativeA:
            firstReal = a.split("+")[0]
        else:
            firstReal = a[0] + tempA.split("-")[0]
        
        if not negativeB:
            secondReal = b.split("+")[0]
        else:
            secondReal = b[0] + tempB.split("-")[0]
        
        # print("first real is ", firstReal)
        # print("second real is ", secondReal)

        firstReal = eval(firstReal)
        secondReal = eval(secondReal)
        
        firstComplex = a.split("+")[1]
        firstComplex = firstComplex[:len(firstComplex) - 1]
        # print("first complex is ", firstComplex)
        firstComplex = eval(firstComplex)

       
        if not negativeB:
             secondComplex = b.split("+")[1]
        else:
            secondComplex = "-" + tempB.split("-")[1]

        secondComplex = secondComplex[:len(secondComplex) - 1]
        # print("second complex is ", secondComplex)
        secondComplex = eval(secondComplex)

        resultReal = firstReal * secondReal - firstComplex * secondComplex 
        resultComplex = firstReal * secondComplex + firstComplex * secondReal

        print("printing real result ", resultReal)
        print("printing result complex ", resultComplex)

        resultFinal = ""
        if resultComplex < 0:
            resultFinal = str(resultReal) + "-" + str(abs(resultComplex)) + "i"
            print("a")
        elif resultComplex == 0:
            resultFinal = str(resultReal)
            print("c")
        else:
            resultFinal = str(resultReal) + "+" + str(resultComplex) + "i"
            print("b")
        print(resultFinal)






# s = Solution()
# # s.complexNumberMultiply("1+1i", "2+2i")
# s.complexNumberMultiply("4+3i", "-3-4i")