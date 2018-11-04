class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        r,w,b = 0,0,0
        for x in A:
            if x == 0:
                r+=1
            elif x== 1:
                w +=1
            elif x==2:
                b +=1
        i = 0
        while r>0:
            A[i] = 0
            i+=1
            r-=1
        while w>0:
            A[i] = 1
            i+=1
            w-=1
        while b>0:
            A[i] = 2
            i+=1
            b-=1
        return A
