# https://www.acmicpc.net/problem/2283
# 구간 자르기
# 2283

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
n_list = []
for _ in range(n):
    a, b = map(int, input().split())
    n_list.append([a,b])

print(n_list)

hi = max(max(n_list))

print(hi)

def fun():


    start = 0
    end = hi 
    


    while start < end:

        sum = 0

        for i in range(n):
            n_start = n_list[i][0]
            n_end = n_list[i][1]

            if n_start == start and n_end == end:
                sum += n_end - n_start
            if n_start > start and n_end < end:
                sum += n_end - n_start
            if n_start < start and n_end < end:
                sum += n_end - start
            if n_start > start and n_end > end:
                sum += end - n_start
            if n_start < start and n_end > end:
                sum += end - start

        print(sum)

        if sum > k:
            start += 1

        elif sum < k:
            start -= 1
            end -= 1

        elif sum == k:
            break

    return

fun()
