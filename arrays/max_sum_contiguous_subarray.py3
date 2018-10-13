def maxSubArray(self, A):
    max_so_far = 0
    max_aux = A[0]
    aux_max_min = A[0]
    for i in range(1, len(A)):
        max_aux = max(A[i], max_aux+A[i])
        max_so_far = max(max_so_far, max_aux)
        aux_max_min = max(aux_max_min, A[i])
    return aux_max_min if max_so_far == 0 else max_so_far