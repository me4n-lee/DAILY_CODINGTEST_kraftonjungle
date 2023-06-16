# https://www.acmicpc.net/problem/1439
# 뒤집기
# 1439

import sys
input = sys.stdin.readline

s_list = list(map(int, input().strip()))

# print(s)

def fun():

    cnt = 1

    for i in range(1, len(s_list)):

        if s_list[i-1] != s_list[i]:
            cnt += 1


    cnt = cnt // 2 

    return cnt

result = fun()
print(result)