class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        root = dict()

        for word in A:
            aux_node = root
            for c in word:
                if c not in aux_node:
                    aux_node[c] = dict()
                    aux_node[c]['count'] = 1
                else:
                    aux_node[c]['count'] += 1
                aux_node = aux_node[c]

        r = []
        for word in A:
            aux_node = root
            s = ''
            for c in word:
                s += c
                if aux_node[c]['count'] == 1:
                    r.append(s)
                    break
                aux_node = aux_node[c]
        
        return r
