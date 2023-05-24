# https://www.acmicpc.net/problem/11652
# 카드
# 11652

import sys
input = sys.stdin.readline

n = int(input())

n_list = []
for _ in range(n):
    a = int(input())
    n_list.append(a)

# print(n_list)

n_list.sort()

max_list = max(n_list)
max_number = 0

# print(n_list)

def fun():

    cnt = 1
    max_number = n_list[0]
    max_cnt = 0

    for i in range(1, n):

        if n_list[i] == n_list[i-1]:
            cnt += 1 

            if max_cnt < cnt:
                max_cnt = cnt
                max_number = n_list[i]
            
        else: 
            cnt = 1


    return max_number

answer = fun()
print(answer)

# print(dp)

# def fun():

#     for i in range(n):
#         num = n_list[i]
#         dp[num] += 1

#     max_dp = max(dp)

#     for i in range(len(dp)):
#         if dp[i] == max_dp:
#             result = i
#             return result

#     # return dp


# answer = fun()
# print(answer)