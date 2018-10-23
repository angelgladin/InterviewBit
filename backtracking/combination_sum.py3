class Solution:
    def combinationSum_aux(self, A, sols, aux, index, target):
        if target == 0:
            l = aux.copy()
            sols.append(l)
        else:
            for i in range(index, len(A)):
                if A[i] > target:
                    break
                aux.append(A[i])
                self.combinationSum_aux(A, sols, aux, i, target-A[i])
                aux.pop()
        
    
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        sols = []
        l = sorted(set(A))
        self.combinationSum_aux(l, sols, [], 0, B)
        return sols