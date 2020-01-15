class Solution:
    def countPrimes(self, n: int) -> int:
        primesList = []
        checkPrime = [True] * (n + 1)
        # checkPrime[0] = checkPrime[1] = False

        if n <= 2:
            return 0
        
        for i in range(2, n):
            currentI = i
            currentCheckPrime = checkPrime[i]
            if checkPrime[i]:
                primesList.append(i)
                # j = i * i
                # while j < n + 1 :
                for j in range(i*i, n + 1, i):
                    checkPrime[j] = False
                    # j = j + i
        # return primesList
        return len(primesList)

# s = Solution()
# result = s.countPrimes(10)
# result = s.countPrimes(20)
# print(result)