# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        count = 1
        return self.hasPathSumHelper(root, sum, 0)
        
    def hasPathSumHelper(self, root: TreeNode, sum: int, sumUpToNow: int) -> bool:
        boolVal = sumUpToNow == sum
        if not root:
            return boolVal
        
        sumUpToNow += root.val
        if sumUpToNow == sum:
            boolVal = True
            return boolVal
        if root.left and root.right:
            leftSide = self.hasPathSumHelper(root.left, sum, sumUpToNow)
            rightSide = self.hasPathSumHelper(root.right, sum, sumUpToNow)
            return leftSide or rightSide
        if root.left and not root.right:
            leftSide = self.hasPathSumHelper(root.left, sum, sumUpToNow)
            return leftSide
        if root.right and not root.left:
            rightSide = self.hasPathSumHelper(root.right, sum, sumUpToNow)
            return rightSide
        else:
            print("HERE WHY HTO")
            print("root", root)
            print("root.left-- > ", root.left)
            print("root.right -- > " , root.right)

# s = Solution()
# givenRoot = TreeNode(1)
# givenRoot.left = TreeNode(2)
# s.hasPathSum(givenRoot, 1)

s = Solution()
givenRoot = TreeNode(5)
leftSide1 = givenRoot.left = TreeNode(4)
rightSide1 = givenRoot.right = TreeNode(8)

leftSide2 = leftSide1.left = TreeNode(11)
# leftSide2_2 = leftSide1.right = None

leftSide3 = leftSide2.left = TreeNode(7)
leftSide3_2 = leftSide2.right = TreeNode(2)

rightSide2 = rightSide1.left = TreeNode(13)
rightSide2 = rightSide1.right = TreeNode(4)

rightSide2_2 = rightSide2.right = TreeNode(1)

# [5,4,8,11,null,13,4,7,2,null,null,null,1]
result = s.hasPathSum(givenRoot, 22)

print("RESULT IS ", result)
# s.hasPathSum(givenRoot, 1)