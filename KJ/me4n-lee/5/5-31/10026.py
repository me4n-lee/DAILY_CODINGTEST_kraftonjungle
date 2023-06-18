# https://www.acmicpc.net/problem/10026
# 적록색약
# 10026

import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    a = list(map(str, input().strip()))
    graph.append(a)

# print(graph)

visit = [[0] * n for _ in range(n)] 

# print(visit)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs_normal():
    stack = []
    cnt = 0

    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                stack.append((i,j))
                visit[i][j] = 1

                while stack:

                    (x, y) = stack.pop()
                    
                    for k in range(4):
                        
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0<= nx < n and 0<= ny < n and visit[nx][ny] == 0:
                            if graph[nx][ny] == graph[x][y]:
                                stack.append((nx,ny))
                                visit[nx][ny] = 1

                cnt += 1

    return cnt

def dfs_blind():
    
    stack = []
    cnt = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'G':
                graph[i][j] = 'R'

    for i in range(n):
        for j in range(n):
            # if graph[i][j] == 'R' or graph[i][j] == 'G':
            if visit[i][j] == 0:
                stack.append((i,j))
                visit[i][j] = 1

                while stack:

                    (x, y) = stack.pop()
                    
                    for k in range(4):
                        
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0<= nx < n and 0<= ny < n and visit[nx][ny] == 0:
                            if graph[nx][ny] == graph[x][y]:
                                stack.append((nx,ny))
                                visit[nx][ny] = 1

                cnt += 1

    return cnt

visit = [[0] * n for _ in range(n)] 
result_normal = dfs_normal()
visit = [[0] * n for _ in range(n)] 
result_blind = dfs_blind()

print(result_normal, result_blind)