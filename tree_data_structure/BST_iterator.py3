# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.__res = self.__preorder(root)
        self.__i = 0
        
    def __preorder(self, root):
        stack = []
        res = []
        current = root
        
        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left
            aux = stack.pop()
            current = aux.right
            res.append(aux)
        return res
                
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.__i < len(self.__res)

    # @return an integer, the next smallest number
    def next(self):
        return self.__res[self.__i]

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
