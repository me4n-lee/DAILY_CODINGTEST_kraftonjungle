# https://www.acmicpc.net/problem/11728
# 배열 합치기
# 11728

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_list = list(map(int, input().split()))
m_list = list(map(int, input().split()))

def fun():

    stack = []

    for i in range(n):
        stack.append(n_list[i])

    for i in range(m):
        stack.append(m_list[i])

    stack.sort()

    return stack

result = fun()
# print(result)

for i in range(len(result)):
    print(result[i], end= " ")