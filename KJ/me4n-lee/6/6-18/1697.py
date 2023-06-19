# https://www.acmicpc.net/problem/1697
# 숨바꼭질
# 1697

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dis = k-n

dp = [0] * (k+1)
dp[n] = 0
# print(dp)

def fun():
        
    for i in range(n-1, -1, -1):
        dp[i] = dp[i+1] + 1

    for i in range(n, k):

        if i%2 != 0:
            dp[i] = min(dp[i-1] + 1, dp[i//2] + 1)

        else:
            dp[i] = dp[i-1] + 1

    return dp

result = fun()
answer = result[k-1] - 1
print(answer)