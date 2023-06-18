# https://www.acmicpc.net/problem/18870
# 좌표 압축
# 18870

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

# print(n_list)

sort_list = sorted(n_list)

# print(sort_list)

cnt = [0] * n

def fun():

    for i in range(n):

        now = n_list[i]
        start = 0
        end = n

        while start > end:
            mid = (start + end) // 2

            if n_list[mid] == now:
                cnt[i] == mid

            if now > n_list[mid]:
                start = mid + 1

            if now < n_list[mid]:

                end = mid - 1
        
    return cnt

result = fun()
print(result)