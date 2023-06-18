# https://www.acmicpc.net/problem/1475
# 방 번호
# 1475

import sys
input = sys.stdin.readline

n_list = list(map(int, input().strip()))

# # print(n_list)

# n = len(n_list)

# def fun():
    
#     cnt = 1

#     for i in range(n):

#         for j in range(i+1, n):

#             if n_list[j] == n_list[i]:
#                 n_list[j] = 0
    
#     for i in range(n):
#         if n_list[i] == 0:
#             cnt += 1

#     return cnt

# result = fun()

# same = 0

# for i in range(n):
#     if n_list[i] == 6 or n_list[i] == 9:
#         same += 1

# result -= (same // 2)

# # print(n_list)            
# print(result)

dp = [0] * 10 

def fun():

    for num in n_list:
        dp[num] += 1

    dp[6] = (dp[6] + dp[9] + 1) // 2
    result = max(dp[:9])

    return result

answer = fun()
print(answer)