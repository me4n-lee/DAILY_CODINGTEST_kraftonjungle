# https://www.acmicpc.net/problem/1926
# 그림
# 1926

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

print(graph)

visit = [[0] * m for _ in range(n)]

print(visit)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b):
    que = deque()
    que.append((a, b))
    
    visit[a][b] = 1
    count = 1

    while que:
        x,  y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    count += 1
                    que.append((nx, ny))

    return count

result = bfs(0,0)
print(result)

