# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        q1 = []
        q2 = []
        q1.append(A)
        i = 0
        # BFS
        while q1 or q2:
            if q1:
                i += 1
            while q1:
                x = q1.pop(0)
                if x.left is not None:
                    q2.append(x.left)
                if x.right is not None:
                    q2.append(x.right)
            
            for x in q2:
                if x.left is None and x.right is None:
                    return i+1
            
            if q2:
                i += 1
            while q2:
                x = q2.pop(0)
                if x.left is not None:
                    q1.append(x.left)
                if x.right is not None:
                    q1.append(x.right)
            
            for x in q1:
                if x.left is None and x.right is None:
                    return i+1
        
        return i
