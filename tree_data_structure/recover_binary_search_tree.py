# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, A):
        stack = []
        current = A
        prev_n = None
        curr_n = None
        r = []
        while stack or current is not None:
            prev_n = curr_n
            while current is not None:
                stack.append(current)
                current = current.left
            aux = stack.pop()
            current = aux.right
            
            curr_n = aux.val
            if prev_n is not None and prev_n > curr_n:
                r.append(curr_n)
                r.append(prev_n)
        a = min(r)
        b = max(r) 
        return [a,b]
