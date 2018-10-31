class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        n = len(A)
        dp_incr = [1]*n
        for i in range(1, n):
            for j in range(i+1):
                if A[i] > A[j]:
                    dp_incr[i] = max(dp_incr[i], dp_incr[j]+1)
        dp_decr = [1]*n
        for i in range(n-1, -1, -1):
            for j in range(i+1,n):
                if A[i] > A[j]:
                    dp_decr[i] = max(dp_decr[i], dp_decr[j]+1)
        max_ = 0
        for i in range(n):
            max_ = max(max_, dp_incr[i]+dp_decr[i]-1)
        return max_

