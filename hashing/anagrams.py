class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        d = dict()
        for i, x in enumerate(A, 1):
            aux = ''.join(sorted(x))
            if aux in d:
                d[aux].append(i)
            else:
                d[aux] = [i]
        r = []
        for _, v in d.items():
            r.append(v)
        return r
