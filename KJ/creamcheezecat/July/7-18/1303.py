""" 
https://www.acmicpc.net/problem/1303<br/>
전쟁-전투<br/>
1303
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N,M = map(int,input().split()) # N 가로 M 세로

# borad = [[0 for _ in range(N)] for _ in range(M)]
borad = []
visited = [[False for _ in range(N)] for _ in range(M)]
for _ in range(M):
    borad.append(input().rstrip())
    

def dfs(x,y,ally):
    if(visited[x][y] == True):
        return 0
    visited[x][y] = True
    cnt = 1

    for i in range(4):        
        nx = x+dx[i]
        ny = y+dy[i]
    
        if 0 <= nx < M and 0 <= ny < N and ally == borad[nx][ny] and visited[nx][ny] == False:
            cnt += dfs(nx,ny,ally)
            
            
    return cnt  
W = 0 # 아군
B = 0 # 적군 

for y in range(N):
    for x in range(M):
        if(visited[x][y] == False):
            if borad[x][y] == 'W' : 
                W += dfs(x,y,'W') ** 2
            else:
                B += dfs(x,y,'B') ** 2
        

print(W, end=" ")
print(B)
#print(borad[0][4])