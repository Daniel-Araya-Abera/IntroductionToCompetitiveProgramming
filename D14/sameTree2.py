# started on Dec 11

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # if (not p.left and p.right ) or (not p.right and p.left):
        print("so p is", p)
        try:
            
            print("p.left:", p.left)
            print("p.right:", p.right)
        except:
            pass
        
        print("so q is", q)
        try:
            
            print("q.left:", q.left)
            print("q.right:", q.right)
        except:
            pass
        # if not(p.left and p.right and q.left and q.right):
        # if p.left is None and p.right is None and q.left is None and q.right is None:
        if p is None and q is None:
            print("BOTH P AND Q ARE NULL")
            print("***********Details***********")
            print("so p is", p)
            try:
               print("p.left:", p.left)
               print("p.right:", p.right)
            except:
                pass

            print("so q is", q)
            try:
 
                print("q.left:", q.left)
                print("q.right:", q.right)
            except:
                pass
            print("***********Details***********")
            return True
        if (not p and q) or (not q and p):
            print("in here")
            return False
        if p != None and q != None:
            if (p.val == None and q.val != None) or (p.val != None and q.val == None):
                return False
            
            
                
            # if p.left == None and p.right == None and q.left == None and q.right == None:
            #     print("in here")
            #     return True
            if p.val != q.val :
                return False
            # if p.left == None and q.left == None:
            #     return True
            a = self.isSameTree(p.left,q.left) 
            b = self.isSameTree(p.right,q.right)
            return a and b
        
            
# s = Solution()
# p = TreeNode(1)
# p.left = TreeNode(2)
# p.right = TreeNode(1)

# q = TreeNode(1)
# q.right = TreeNode(1)
# q.right = TreeNode(2)

# final = s.isSameTree(p,q)
# print("final is")
# print(final)
s = Solution()
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(1)

q = TreeNode(1)
q.right = TreeNode(1)
q.right = TreeNode(1)

final = s.isSameTree(p,q)
print("final is")
print(final)