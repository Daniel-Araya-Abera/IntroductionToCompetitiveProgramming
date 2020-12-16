class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = []
        start = 0
        for i in range(1,len(expression)):
            if expression[i] == "+":
                fractions.append(expression[start:i])
                start = i + 1
            elif expression[i] == "-":
                fractions.append(expression[start:i])
                start = i
        fractions.append(expression[start:len(expression)])
        
        numerators = []
        denominators = []
        for each in fractions:
            curr = each.split("/")
            if len(curr) != 1:
                denominators.append(curr[1])
            numerators.append(curr[0])
        
        curr_gcd = int(denominators[0])
    
        for i in range(1, len(denominators)):
            curr_gcd = self.gcd(curr_gcd, denominators[i])

        product = 1
        for each in denominators:
            product *= int(each)
        
        curr_lcm = self.lcm(product,1,int(curr_gcd))
        
        summ = 0
        for i in range(len(numerators)):
            curr = curr_lcm // int(denominators[i])
            curr *= int(numerators[i])
            summ += curr

        if summ == 0:
            return "0/1"
        res_gcd = self.gcd(abs(summ), abs(curr_lcm))
        summ = summ // res_gcd
        curr_lcm = curr_lcm // res_gcd
        res = str(summ) + "/" + str(curr_lcm)
        return res
            
    
    def gcd(self, a, b):
        a, b = int(a), int(b)
        a, b= max(a,b), min(a,b)
        r = a % b
        while r:
            a = b
            b = r
            r = a % b
        return b
        
    def lcm(self, a, b, gcd):
        if a * b == gcd:
            return a * b
        return (a * b) // gcd
    