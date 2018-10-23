class Solution:
    
    def subsets_aux(self, A, all_sets, aux, index):
        l = aux.copy()
        all_sets.append(l)
        for i in range(index, len(A)):
            aux.append(A[i])
            self.subsets_aux(A, all_sets, aux, i+1)
            aux.pop()
    
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort()
        all_sets = []
        self.subsets_aux(A, all_sets, [], 0)
        return all_sets
