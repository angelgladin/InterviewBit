class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        n = (A*2)-1
        layer = A
        m = [[0]*n for x in range(n)]
        
        top = 0
        bottom = n-1
        left = 0
        right = n-1
        while layer > 0:
            for j in range(left, right+1):
                m[top][j] = layer
                m[bottom][j] = layer
            top += 1
            bottom -= 1
            for i in range(top, bottom+1):
                m[i][left] = layer
                m[i][right] = layer
            left += 1
            right -= 1

            layer -= 1
        return m