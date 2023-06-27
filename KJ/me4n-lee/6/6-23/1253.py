# https://www.acmicpc.net/problem/1253
# 좋다
# 1253

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

# print(n_list)

n_list.sort()

# def fun():
    
#     result = []

#     for i in range(n):
#         for j in range(i+1, n):
            
#             if n_list[i] + n_list[j] in n_list and n_list[i] != n_list[j]:
#                 hi = n_list[i] + n_list[j]
#                 if hi not in result:
#                     result.append(hi)

#     return result

# answer = fun()
# print(len(answer))

def fun():

    count = 0

    for i in range(n):

        start = 0
        end = n - 1

        while start < end:
            
            if start == i:
                start += 1
                continue

            if end == i:
                end -= 1
                continue

            num_sum = n_list[start] + n_list[end]

            if num_sum == n_list[i]:
                count += 1
                break
            
            elif num_sum < n_list[i]:
                start += 1
            
            else:
                end -= 1

    return count

result = fun()
print(result)