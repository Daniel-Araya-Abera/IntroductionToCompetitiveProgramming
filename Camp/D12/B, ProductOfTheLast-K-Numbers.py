class ProductOfNumbers:

    def __init__(self):
        self.stack = []
        self.productArray = []

    def add(self, num: int) -> None:
        self.stack.append(num)

        if num == 0:
            self.productArray = []
        else:
            if len(self.productArray) == 0: 
                self.productArray.append(num)
            else:
                productFound = self.productArray[-1] * num
                self.productArray.append(productFound)


    def getProduct(self, k: int) -> int:
        if k == len(self.productArray):
            return self.productArray[-1]
        elif k > len(self.productArray) :
            return 0
        else:
            return self.productArray[len(self.productArray) - 1] // self.productArray[len(self.productArray) - 1 - k] 
        
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)