# https://www.acmicpc.net/problem/1780
# 종이의 개수
# 1780

import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

print(graph)

visit = [[0] * n for _ in range(n)]

print(visit)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(a, b, hi):

    cnt = 0
    stack = []
    for i in range(n):
        for j in range(n):
            stack.append((i, j))

            while stack:

                x, y = stack.pop()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] == hi and visit[nx][ny] == 0:
                            visit[nx][ny] = 1
                            stack.append((nx, ny))

            cnt += 1

    return cnt



for i in range(-1, 2):
    result = dfs(0,0,i)
    print(result)