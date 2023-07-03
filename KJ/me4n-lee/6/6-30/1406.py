# https://www.acmicpc.net/problem/1269
# 대칭 차집합
# 1269

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

def fun():

    a_set = set(a_list)
    b_set = set(b_list)
    #교집합 개수

    count = a_set.intersection(b_set)

    result = len(a_list) + len(b_list) - (len(count) * 2)

    return result

answer = fun()
print(answer)