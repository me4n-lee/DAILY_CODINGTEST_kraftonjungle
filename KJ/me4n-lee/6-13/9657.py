# https://www.acmicpc.net/problem/9657
# 돌 게임3
# 9657

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 1001

# dp가 0이면 cy, 1이면 sk
def fun():

    dp[1] = 1
    dp[2] = 0
    dp[3] = 1
    dp[4] = 1

    # for i in range(5, n+1):

    #     dp[i] = max(dp[i-1],dp[i-3],dp[i-4]) + 1

    # print(dp)

    for i in range(5, n+1):
        if dp[i-1] == 0 or dp[i-3] == 0 or dp[i-4] == 0:
            dp[i] = 1
        else:
            dp[i] = 0

    if dp [n] == 1:
        return "SK"
    else:
        return "CY"


result = fun()
print(result)