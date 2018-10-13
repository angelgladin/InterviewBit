class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        m = [[-1]*A for _ in range(A)]
        k = 1

        top = 0
        bottom = A-1
        left = 0
        right = A-1
        direction = -1

        while top <= bottom and left <= right:
            direction = (1+direction)%4
            if direction == 0:
                for j in range(left, right+1):
                    m[top][j] = k
                    k += 1
                top += 1
            elif direction == 1:
                for i in range(top, bottom+1):
                    m[i][right] = k
                    k += 1
                right -= 1
            elif direction == 2:
                for j in range(right, left-1, -1):
                    m[bottom][j] = k
                    k += 1
                bottom -= 1
            elif direction == 3:
                for i in range(bottom, top-1, -1):
                    m[i][left] = k
                    k += 1
                left += 1
            #print(m)
        return m

