# https://www.acmicpc.net/problem/13270
# 피보나치 치킨
# 13270

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n)

def d(n):

    for i in range(n):

        if i == 0:
            dp[i] = 0
        elif i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        else:
            dp[i] = dp[i-1] + dp[i-2]
    
    return dp

def min(n):
        
    min = 0

    if n % 2 == 0:
        min = int(n / 2)
    else:
        min = int(n / 2) + 1
    
    return min

def max(n):    

    max = 0

    while n != 0:

        if n == 3:
            max += 2
            n = 0

        if n == 2:
            max += 1
            n = 0

        for i in range(len(dp)):
            if n > dp[i]:
                n = n - dp[i-1]
                max += dp[i-2]

            break

    return max

print(d(n))
print(min(n))
print(max(n))