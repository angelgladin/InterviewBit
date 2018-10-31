class Solution:
    # @param A : integer
    # @return an integer
    def climb_stairs_aux(self, i, memo):
        if i in memo:
            return memo[i]
        memo[i] = self.climb_stairs_aux(i-1, memo) + self.climb_stairs_aux(i-2, memo)
        return memo[i]

    def climbStairs(self, A):
        memo = dict()
        memo[1] = 1
        memo[2] = 2
        memo[3] = 3
        return self.climb_stairs_aux(A, memo)