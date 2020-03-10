"""
Thomas Morris
Implement a program which returns i) inorder and ii) preorder traversal of 
a given a binary tree. Note that you should follow the code fragment style 
to create your program below and can use recursive (or iterative) function. 
November 8th, 2019
"""

#definion for a binary tree node
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Traversal(object):                
    def inorderTraversal(self,root):
        #:Type root: TreeNode
        #:rtype: List[int]
        #left, root, right
        #recursively traverse the tree
        L = []
        if root:
            L = self.inorderTraversal(root.left)
            L.append(root.val)
            L = L + self.inorderTraversal(root.right)
        return L
        
    
    def preorderTraversal(self,root):
        #:Type root: TreeNode
        #:rtype: List[int]
        #root, left, right
        #recursively traverse the tree
        L = []
        if root:
            L.append(root.val)
            L = L + self.preorderTraversal(root.left)
            L = L + self.preorderTraversal(root.right)
        return L
    
if __name__ == '__main__':
    N = TreeNode(1)
    N.right = TreeNode(2)
    N.right.left = TreeNode(3)
    T = Traversal()
    print(T.inorderTraversal(N))
    print(T.preorderTraversal(N))
    