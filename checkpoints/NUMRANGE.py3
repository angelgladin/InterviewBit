def numRange(A, B, C):
    n = len(A)
    dp = [0]*n
    dp[0] = A[0]
    for i in range(1, n):
        dp[i] = A[i] + dp[i-1]
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if i == 0:
                r = dp[j] 
            else:
                r = dp[j] - dp[i-1]
            if r>=B and r<=C:
                ans +=1
            if r>C:
                break
    return ans