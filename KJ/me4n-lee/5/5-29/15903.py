# https://www.acmicpc.net/problem/15903
# 카드 합체 놀이
# 15903

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = list(map(int,input().split()))

# print(n_list)

n_list.sort()

def fun():

    for k in range(m):


        n_list.sort()

        sum_n = n_list[0] + n_list[1]
        n_list[0] = sum_n
        n_list[1] = sum_n

        # print(n_list)

    return n_list

result = fun()
print(sum(result))