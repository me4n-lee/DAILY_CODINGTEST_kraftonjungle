# https://www.acmicpc.net/problem/2847
# 게임을 만든 동준이
# 2847

import sys
input = sys.stdin.readline

n = int(input())

n_list = []
for _ in range(n):
    a = int(input())
    n_list.append(a)

# print(n_list)

n_list.reverse()

# print(n_list)

def fun():

    cnt = 0

    for i in range(n):
        if i != 0:
            if n_list[i] > n_list[i-1]:
                a = n_list[i] - n_list[i-1] + 1
                n_list[i] = n_list[i] - a
                cnt += a
            elif n_list[i] == n_list[i-1]:
                n_list[i] = n_list[i] - 1
                cnt += 1
    
    return cnt 

result = fun()
print(result)