# https://www.acmicpc.net/problem/2217
# 로프
# 2217

import sys
input = sys.stdin.readline

n = int(input())

n_list = []
for _ in range(n):
    a = int(input())
    n_list.append(a)

# def fun():

#     start = 0
#     end = max(n_list)

#     max_weight = 0

#     while start <= end:
#         mid = (start + end) // 2
#         weight = 0

#         for i in range(n):

#             if n_list[i] > mid:
#                 weight += mid

#             if n_list[i] <= mid:
#                 weight += n_list[i]

#         if weight >= max_weight:
#             max_weight = weight
#             start = mid + 1

#         else:
#             end = mid - 1

#     return max_weight

n_list.sort()

def fun():

    result = 0
    max_result = 0

    for i in range(n):
        result = n_list[i] * (n - i)

        if max_result < result:
            max_result = result

    return max_result

result = fun()
print(result)