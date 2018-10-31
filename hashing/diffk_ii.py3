'''
# "Naive" aproach
class Solution:
    def binary_search(self, A, start, end, k):
        while start<=end:
            mid = start +(end-start)//2
            if A[mid] == k:
                return True
            elif A[mid] > k:
                end = mid-1
            else:
                start = mid+1
        return False
    
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        n = len(A)
        l = sorted(list(A))
        for i in range(n):
            if self.binary_search(l, i+1, n-1, l[i]+B):
                return 1
        return 0
'''

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        # The "correct" answer.
        s = set()
        for x in A:
            if (x+B) in s or (x-B) in s:
                return 1
            s.add(x)
        return 0
