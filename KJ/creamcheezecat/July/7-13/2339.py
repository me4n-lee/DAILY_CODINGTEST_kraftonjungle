""" 
https://www.acmicpc.net/problem/2339<br/>
석판 자르기<br/>
2339
"""

import sys
input = sys.stdin.readline


N = int(input())

stones = []

checking = []
jewel = 0
impuri = 0
for _ in range(N):
    checking = list(map(int,input().split()))
    jewel += checking.count(2)
    impuri += checking.count(1)
    stones.append(checking)

def fun(x,y,nx,ny,cutting):
    jewel = 0
    impuri = 0
    # 조건 탐색
    for i in range(y,ny):
        for j in range(x,nx):
            if stones[i][j] == 2:
                jewel += 1
            elif stones[i][j] == 1:
                impuri += 1
    
    # 재귀 했을시 끝내는 조건
    if jewel == 1 and impuri == 0:
        return 1
    elif jewel == 1 and impuri == 1:
        return 0
    elif jewel == 0:
        return 0
    elif jewel > 2 and impuri == 0:
        return 0

    # 재귀 조건시에만 재귀
    result = 0
    flag = False
    for i in range(y,ny):
        for j in range(x,nx):
            if stones[i][j] == 1:
                if cutting == True:
                    if j != x and j != nx:
                        flag = True
                        for k in range(y,ny):
                            if stones[k][j] == 2:
                                flag = False
                                break
                        if flag == True:
                            result = result + fun(x,y,j,ny, False)*fun(j+1,y,nx,ny,False)
                else:
                    if i != x and x != nx:
                        flag = True
                        for k in range(x,nx):
                            if stones[i][k] == 2:
                                flag = False
                                break
                        if flag == True:
                            result = result + fun(x,y,nx,i, True)*fun(x,i+1,nx,ny,True)
                            
                            
    return result
                         


if jewel == 1 and impuri == 0:
    print(1)
else:
    resultA = fun(0,0,N,N,True)
    resultB = fun(0,0,N,N,False)

    if (resultA + resultB) == 0:
        print(-1)
    else:
        print( resultA + resultB )

#print(stones[0][5])