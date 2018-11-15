class Solution:
    # @param A : integer
    # @return a strings
    def parse(self, A):
        n = len(A)
        if n == 1:
            return '11'
        buckets = []
        c = 1
        prev = None
        for i in range(n):
            if prev is not None:
                if prev == A[i]:
                    c += 1
                    if i == n-1:
                        buckets.append((c, A[i],))
                else:
                    buckets.append((c, A[i-1],))
                    c = 1
                    if i == n-1:
                        buckets.append((1, A[i],))
            prev = A[i]
        r = ''
        for (c, x) in buckets:
            r += str(c) + x
        return r

    def countAndSay(self, A):
        seq = ['' for _ in range(A)]
        seq[0] = '1'
        for i in range(1, A):
            seq[i] = self.parse(seq[i-1])
        return seq[A-1]