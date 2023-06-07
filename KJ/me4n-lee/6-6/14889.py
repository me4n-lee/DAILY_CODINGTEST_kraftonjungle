# https://www.acmicpc.net/problem/14889
# 스타트와 링크
# 14889

import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

print(graph)



def fun():

    n_list = []

    for i in range(n):
        for j in range(i, n):
            a = graph[i][j] + graph[j][i]

            if a != 0:
                n_list.append(a)

    print(n_list)

    n_list.sort()
    print(sum(n_list))

    # print(sum_status)
    status = sum(n_list) / 2
    start = 0

    # for i in range(n):

        



    return n_list



result = fun()

print(result)