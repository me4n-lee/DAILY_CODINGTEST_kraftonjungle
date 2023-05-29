# https://www.acmicpc.net/problem/1431
# 시리얼 번호
# 1431

import sys
input = sys.stdin.readline

n = int(input())

n_list = []

for _ in range(n):
    a = input().split()
    n_list.append(a)


print(n_list)



def fun():

    serial = []
    sub = 0

    for i in range(n):
        sub = n_list[i]
        serial = [char for char in sub[0]]
        print(serial)
        # serial = sub.split()

        # print(serial)

    return

fun()