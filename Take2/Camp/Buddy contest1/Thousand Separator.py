class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000:
            return str(n)
        res = []
        while n > 0:
            num = n % 1000
            n = n // 1000
            curr = str(int(num))
            while n > 0 and len(curr) < 3:
                curr = "0" + curr
            res.append(curr)
        
        res.reverse()
        return ".".join(res)
        