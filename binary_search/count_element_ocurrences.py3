class Solution:
    def binary_search_mod(self, arr, x, find_first):
        low = 0
        high = len(arr)-1
        result = -1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] == x:
                result = mid
                if find_first:
                    high = mid-1
                else:
                    low = mid+1
            elif arr[mid] > x:
                high = mid-1
            else:
                low = mid+1
        return result
    
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        first_index = self.binary_search_mod(A, B, True)
        last_index = self.binary_search_mod(A, B, False)
        if first_index + last_index == -2:
            return 0
        return last_index - first_index + 1