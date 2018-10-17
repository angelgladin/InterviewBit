class Solution:
    
    def binary_search_mod(self, A, x, first_index):
        low = 0
        high = len(A)-1
        result = -1
        while low <= high:
            mid = (low+high)//2
            if A[mid] == x:
                result = mid
                if first_index:
                    high = mid-1
                else:
                    low = mid+1
            elif A[mid] < x:
                low = mid+1
            else:
                high = mid-1
        return result

    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        first_index = self.binary_search_mod(A, B, True)
        last_index = self.binary_search_mod(A, B, False)
        return [first_index, last_index]