class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1 or n == 2:
            return 1
        
        memoizer = [-1] *  (n + 1)
        memoizer[0] = 0
        memoizer[1] = 1
        memoizer[2] = 1
        
 
        
        return self.tribonacciHelper(n, memoizer)
        
    def tribonacciHelper(self, n: int, memoizer: List) -> int:
        if n == 0:
            return 0
        
        if n == 1 or n == 2:
            return 1
        
        if memoizer[n] != -1:
            return memoizer[n]
        else:
            if memoizer[n - 1] == -1:
                memoizer[n - 1] = self.tribonacciHelper(n - 1, memoizer)
            if memoizer[n - 2] == -1:
                memoizer[n - 2] = self.tribonacciHelper(n - 2, memoizer)
            if memoizer[n - 3] == -1:
                memoizer[n - 3] = self.tribonacciHelper(n - 3, memoizer)
            
            # return memoizer[n - 1] + memoizer[n - 2] + memoizer[n - 3]
            result = memoizer[n - 1] + memoizer[n - 2] + memoizer[n - 3]
            memoizer[n] = result
            return memoizer[n]
        