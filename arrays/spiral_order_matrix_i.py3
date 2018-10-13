class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        n, m = len(A), len(A[0])
        # right->0, down->1, left->2, up->3 
        direction = 0

        top = 0
        bottom = n-1
        left = 0
        right = m-1

        r = []
        while top <= bottom and left <= right:
            if direction == 0:
                for j in range(left, right+1):
                    r.append(A[top][j])
                top += 1
            elif direction == 1:
                for i in range(top, bottom+1):
                    r.append(A[i][right])
                right -= 1
            elif direction == 2:
                for j in range(right, left-1, -1):
                    r.append(A[bottom][j])
                bottom -= 1
            elif direction == 3:
                for i in range(bottom, top-1, -1):
                    r.append(A[i][left])
                left += 1
            direction = (direction + 1) % 4
        return r



