# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.stack = []
        self.visited = {}
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def increasingBSTHelper(root: TreeNode) -> TreeNode:
            if root:
                if root.left:
                    increasingBSTHelper(root.left)          
                if root.val not in self.visited:
                    self.stack.append(root.val)
                    self.visited[root.val] = 1     
                if root.right:
                    increasingBSTHelper(root.right)      
        
        increasingBSTHelper(root)
        
        parent = TreeNode(self.stack.pop(0))
        rest = parent
        while len(self.stack) > 0:
            newNode = TreeNode(self.stack.pop(0))
            rest.right = newNode
            rest = newNode
        return parent