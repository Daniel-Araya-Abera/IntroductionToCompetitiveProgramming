# Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/
# Difficulty: Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        
        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.left
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        smallestNode = self.stack.pop()
        if smallestNode.right:
            self.addNodes(smallestNode.right)
        return smallestNode.val
    
    def addNodes(self, currentNode):
        self.stack.append(currentNode)
        if currentNode.left:
            return self.addNodes(currentNode.left)
        
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()