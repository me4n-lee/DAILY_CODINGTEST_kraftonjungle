# https://www.acmicpc.net/problem/11501
# 주식
# 11501

import sys
input = sys.stdin.readline

# t = int(input())
n = int(input())
n_list = list(map(int, input().split()))

def fun():

    benefit = 0
    benefit = benefit - n_list[0]

    n_list[0] = 0


    for i in range(1, n):

        max_list = max(n_list)

        if n_list[i-1] < n_list[i]:

            if n_list[i] == max_list:
                benefit = benefit + (n_list[i] * (i-1))
                n_list[i] = 0

            else:
                benefit = benefit - n_list[i]
                n_list[i] = 0

        else:
            benefit = benefit + n_list[0]

        print(n_list)

    return benefit

reseult = fun()
print(reseult)