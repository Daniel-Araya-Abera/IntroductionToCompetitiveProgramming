# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left , p , q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right , p , q)
        return root
root = TreeNode(2)
root.left = TreeNode(1)

s = Solution()
p = TreeNode(2)
q = TreeNode(1)
result = s.lowestCommonAncestor(root, p, q)
print(result)