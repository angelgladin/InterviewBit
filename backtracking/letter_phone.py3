class Solution:
    def letterCombinations_aux(self, A, chars, sols, aux, index):
        if index >= len(A):
            l = ''.join(aux)
            sols.append(l)
        else:
            for x in chars[A[index]]:
                aux.append(x)
                self.letterCombinations_aux(A, chars, sols, aux, index+1)
                aux.pop()
    
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        chars = [['0'], ['1'], ['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        sols = []
        B = [int(x) for x in A]
        self.letterCombinations_aux(B, chars, sols, [], 0)
        return sols

