class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        A.sort()
        i = 0
        while i < n-1:
            if A[i] != A[i+1] and A[i] == n-i-1:
                return 1
            i+=1
        if A[n-1] == 0:
            return 1
        return -1