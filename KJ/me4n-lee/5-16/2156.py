# https://www.acmicpc.net/problem/2156
# 포도주 시식
# 2156

import sys
input = sys.stdin.readline

n = int(input())

n_list = []
for _ in range(n):
    a = int(input())
    n_list.append(a)

dp = [0 for _ in range(n+1)]

def fun():
    dp[0] = n_list[0]
    dp[1] = dp[0] + n_list[1]

    for i in range(2,n):
        dp[i] = max(dp[i-1], dp[i-3]+n_list[i-1]+n_list[i], dp[i-2]+n_list[i])

fun()
result = dp[n-1]
print(result)