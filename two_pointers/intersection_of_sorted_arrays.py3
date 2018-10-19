class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        n_i, n_j = len(A), len(B)
        i, j = 0, 0
        r = []
        while i < n_i and j < n_j:
            if A[i] == B[j]:
                r.append(A[i])
                i += 1
                j += 1
            elif A[i] < B[j]:
                i += 1
            else:
                j += 1
        return r

