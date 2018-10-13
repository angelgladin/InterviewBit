import math

class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        r = set()
        n = math.sqrt(A)
        for i in range(1, math.ceil(math.sqrt(A))+1):
            x = A%i
            if x == 0:
                r.add(i)
                r.add(A//i)
        return sorted(r)
