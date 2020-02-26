# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minOfTwoDistinctNums(self,firstNum, secondNum):
        if firstNum < secondNum:
            return firstNum
        return secondNum
    
    depthCollections = {}
    
    def findBottomLeftValue(self, root: TreeNode) -> int:
        firstResult = secondResult = 0
        if root.left != None:
            print("left isn't empty")
            if not(root.left.left or root.left.right):
                firstResult = root.left.val
                print("GOT HERE GREAT, FIRST VAL:", firstResult)
            else:
                firstResult = self.findBottomLeftValue(root.left) 
            print("first result is ", firstResult)
        if root.right != None:
            print("right isn't empty")
            if not(root.right.left or root.right.right):
                secondResult = root.right.val
                print("GOT HERE GREAT, SECOND VAL:", secondResult)
            else:
                secondResult = self.findBottomLeftValue(root.right)

            print("second result is ", secondResult)
        print("here now")
        return self.minOfTwoDistinctNums(firstResult, secondResult)
        