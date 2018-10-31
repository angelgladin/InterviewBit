class Solution:
    # @param A : string
    # @return an integer
    def numDecodings_aux(self, A, k, n, dp):
        if k == n:
            return 1
        elif k > n:
            return 0
        if dp[k] == -1:
            count = 0
            if A[k] > 0 and A[k] < 10:
                count += self.numDecodings_aux(A, k+1, n, dp)
            if k+1 < n and ((A[k] == 2 and A[k+1] < 7) or (A[k] == 1 and A[k+1] < 10)):
                count += self.numDecodings_aux(A, k+2, n, dp)
            dp[k] = count
        return dp[k]

    def numDecodings(self, A):
        l = [int(x) for x in A]
        n = len(A)
        dp = [-1]*(n)
        self.numDecodings_aux(l, 0, n, dp)
        return dp[0]
