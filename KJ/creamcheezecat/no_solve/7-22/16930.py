""" 
https://www.acmicpc.net/problem/16930
달리기
16930
"""

import sys
input = sys.stdin.readline
from collections import deque

# NxM 체육간  . 빈칸 # 는 벽
# 매초 마다 한 방향을 1 ~ K 칸 이동
# 최소 시간

N,M,K = map(int , input().split())

board = []
#visited = [[False for _ in range(N)] for _ in range(M)]
for _ in range(N):
    board.append(input().rstrip())
    
startx, starty, endx, endy = map(int , input().split())

def bfs():
    q = deque()
    q.append((startx - 1, starty - 1, 0))  # x, y, 이동횟수
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[starty - 1][startx - 1] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y, cnt = q.popleft()
        
        if x == endx - 1 and y == endy - 1:
            return cnt
        
        for i in range(4):
            for k in range(1, K + 1):
                nx = x + (dx[i] * k)
                ny = y + (dy[i] * k)

                if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
                    if board[ny][nx] == '#':
                        break  # 벽을 만나면 해당 방향으로의 추가적인 이동을 중단합니다.
                    elif visited[ny][nx] == False:
                        visited[ny][nx] = True
                        q.append((nx, ny, cnt + 1))
                    
                    
                else:
                    break  # 범위를 벗어나거나 이미 방문한 위치라면 해당 방향으로의 추가적인 이동을 중단합니다.
    
    return -1

print(bfs())