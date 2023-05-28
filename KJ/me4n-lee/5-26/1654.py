# https://www.acmicpc.net/problem/1654
# 랜선 자르기
# 1654

import sys
input = sys.stdin.readline

k, n = map(int,input().split())

k_list = []
for _ in range(k):
    a = int(input())
    k_list.append(a)

# print(k_list)

def fun():

    result = 0
    cnt = 0

    start = 1
    end = max(k_list)
    
    while start <= end:
        mid = (start + end) // 2
        cnt = 0

        for i in range(k):
            cnt += k_list[i] // mid

        # print(cnt)

        if cnt >= n:
            result = mid
            start = mid + 1

        else:
            end = mid -1

    return result

answer = fun()
print(answer)