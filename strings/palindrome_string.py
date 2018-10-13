class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        r = ''
        for x in A:
            if x.isalnum():
                r += x.lower()
        n = len(r)
        for i in range(n):
            if r[i] != r[n-i-1]:
                return 0
        return 1