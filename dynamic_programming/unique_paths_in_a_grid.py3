class Solution:
    # @param A : list of list of integers
    # @return an integer
    def helper(self, A, n, m, i, j, dp):
        if i == n-1 and j == m-1 and A[i][j] == 0:
            return 1
        if i>=n or j>=m:
            return 0
        if A[i][j] == 1:
            return 0
        if dp[i][j] == -1:
            dp[i][j] = self.helper(A, n, m, i+1, j, dp) + self.helper(A, n, m, i ,j+1, dp)
        return dp[i][j]

    def uniquePathsWithObstacles(self, A):
        n, m = len(A), len(A[0])
        dp = [[-1]*m for _ in range(n)]
        return self.helper(A, n, m, 0, 0, dp)
