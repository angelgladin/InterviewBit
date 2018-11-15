# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        if A is None:
            return []
        r = []
        q1, q2 = [], []
        q1.append(A)
        while q1 or q2:
            if q1:
                r.append([x.val for x in q1])
            while q1:
                aux = q1[0]
                q1.pop(0)
                if aux.left is not None:
                    q2.append(aux.left)
                if aux.right is not None:
                    q2.append(aux.right)
            if q2:
                r.append([x.val for x in q2])
            while q2:
                aux = q2[0]
                q2.pop(0)
                if aux.left is not None:
                    q1.append(aux.left)
                if aux.right is not None:
                    q1.append(aux.right)
        return r
