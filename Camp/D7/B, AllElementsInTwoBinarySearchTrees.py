# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        givenList1 = givenList2 = []
        firstList = self.getInorderTraversal(root1)
        secondList = self.getInorderTraversal(root2)
        
        result = []
        for i in range(len(firstList)):
            result.append(firstList[i])
        
        for j in range(len(secondList)):
            result.append(secondList[j])
        
        result.sort()
        return result

    
    def getInorderTraversalHelper(self, root: TreeNode,result) -> int:
        if root:
            leftSide = root.left
            rightSide = root.right
            if leftSide:
                self.getInorderTraversalHelper(root.left,result)
            result.append(root.val)
            if rightSide:
                self.getInorderTraversalHelper(root.right,result)

        return result
        
    def getInorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root:
            self.getInorderTraversalHelper(root.left,result)
            result.append(root.val)
            self.getInorderTraversalHelper(root.right,result)
        
        return result
