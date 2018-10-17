class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        n = len(A)
        max_ = max(A)
        msb = 0
        while max_ > 0:
            msb += 1
            max_ >>= 1
        mask = (1<<msb)-1
        for i in range(n):
            A[i] <<= msb
        for i in range(n):
            j = A[i]>>msb
            A[i] = (~mask&A[i])|(A[j]>>msb)
        for i in range(n):
            A[i] &= mask
        return A