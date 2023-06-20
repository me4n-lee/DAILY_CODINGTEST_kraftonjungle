# https://www.acmicpc.net/problem/9461
# 파도반 수열
# 9461

import sys
input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
# n = int(input())

# dp = [0] * (n+1)

def fun(n):

    dp = [0] * (n)

    # dp[0] = 1
    # dp[1] = 1
    # dp[2] = 1
    # dp[3] = 2
    # dp[4] = 2

    for i in range(n):

        if i == 0 or i == 1 or i == 2:
            dp[i] = 1

        elif i == 3 or i == 4:
            dp[i] = 2

        else:
            dp[i] = dp[i-1] + dp[i-5]

    return dp

# result = fun()
# print(result)

t = int(input())
answer = []
for _ in range(t):

    n = int(input())
    result = fun(n)
    answer.append(result[n-1])

for i in range(len(answer)):
    print(answer[i])