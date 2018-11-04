class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        r = []
        n = len(A)
        for l in range(n):
            aux = []
            for k in range(l+1):
                i = k
                j = l-k
                aux.append(A[i][j])
            r.append(aux)
        for l in range(n-1):
            aux = []
            for k in range(n-l-1):
                i = k+1+l
                j = n-1-k
                aux.append(A[i][j])
            r.append(aux)
        return r
