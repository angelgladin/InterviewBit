class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        stack = []
        n = len(A)
        for x in A:
            stack.append(x)
        r = ''
        for x in range(n):
            r += stack.pop()
        return r         
