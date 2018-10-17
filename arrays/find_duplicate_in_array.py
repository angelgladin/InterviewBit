class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        a_aux = [0] * (n+1)
        for i in range(n):
            a_aux[A[i]] += 1
        i = 0
        for x in a_aux:
            if x > 1:
                return i
            i+=1
        return -1
