# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        #inorder (left, root, right)
        current = A
        stack = []
        res = []
        while stack or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left
            aux = stack.pop()
            current = aux.right
            res.append(aux.val)
        return res
