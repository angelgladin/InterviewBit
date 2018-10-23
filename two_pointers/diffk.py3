class Solution:
    def binary_serach(slef, A, start, end, k):
        while start <= end:
            mid = start + (end - start)//2
            if A[mid] == k:
                return True
            elif A[mid] > k:
                end = mid-1
            else:
                start = mid+1
        return False
    
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        n = len(A)
        for i in range(n-1):
            if self.binary_serach(A, i+1, n-1, A[i]+B):
                return 1
        return 0