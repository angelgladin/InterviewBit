class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        n = len(A)
        max_so_far = 1
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                if A[j] < A[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            max_so_far = max(max_so_far, dp[i])
        return max_so_far