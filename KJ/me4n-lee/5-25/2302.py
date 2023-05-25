# https://www.acmicpc.net/problem/2302
# 극장 좌석
# 2302

import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline

n = int(input())
m = int(input())

m_list = []
for _ in range(m):
    a = int(input())
    m_list.append(a)

# print(m_list)

# def fibo(n):

#     ans = 0

#     if n == 0:
#         ans = 1
#     if n == 1:
#         ans = 1
#     if n == 2:
#         ans = 2
#     if n == 3:
#         ans = 3
#     if n > 3:
#         ans = fibo(n-1) + fibo(n-2)

#     return ans

def fibo(n):
    if n <= 0:
        return 1
    
    dp = [0] * (n+1)

    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]

def fun():

    result = []

    for i in range(m):
        if i == 0:
            first = m_list[i] - 1
            result.append(fibo(first))
        else:
            chai = m_list[i] - m_list[i-1] -1
            result.append(fibo(chai))

    # print(m_list[-1])
    # last = n - m_list[-1]
    # print(last)
    if m > 0:
        last = n - m_list[-1]
        result.append(fibo(last))
    else:
        result.append(fibo(n))

    return result

answer = fun()
# print(answer)

goal = 1

for i in range(len(answer)):
    if answer[i] != 0:
        goal *= answer[i]

print(goal)