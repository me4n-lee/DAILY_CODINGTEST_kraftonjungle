# https://www.acmicpc.net/problem/3273
# 두 수의 합
# 3273

import sys
input = sys.stdin.readline

n = int(input())

n_list = list(map(int, input().split()))

x = int(input())


# print(n_list)


# def fun():

#     cnt = 0

#     for i in range(n):
#         for j in range(i, n):
#             if n_list[i] + n_list[j] == x:
#                 cnt += 1 

#     return cnt

# result = fun()
# print(result)


n_list.sort()

def fun():

    cnt = 0
    left = 0
    right = n-1

    while left<right:
        result = n_list[left] + n_list[right]

        if result == x:
            cnt += 1
            left += 1
            right -= 1
        elif result < x:
            left += 1
        else:
            right -= 1

    return cnt

result = fun()
print(result)
