# https://www.acmicpc.net/problem/11057
# 오르막 수
# 11057

import sys
input = sys.stdin.readline

n = int(input())


dp = [0] * (n+1)

def result():

    n_result = 0

    for i in range(1, n+1):

        if i == 1:
            dp[i] = 10
            n_result = 10

        else:
            n_result *= (11-i) / i
            dp[i] = sum(dp) + n_result

result()
print(dp)

# def fun():

#     result = 0

#     if n == 2:
#         dp[2] = (10*9 / 2) + dp[1]

#     if n > 3:


