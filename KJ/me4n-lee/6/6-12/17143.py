# https://www.acmicpc.net/problem/17143
# 낚시왕
# 17143

import sys
input = sys.stdin.readline

r, c, m = map(int,input().split())

shark = []
s = []
d = []
z = []
for _ in range(m):
    m_list = list(map(int, input().split()))
    shark.append([m_list[0], m_list[1]])
    s.append(m_list[2])
    d.append(m_list[3])
    z.append(m_list[4])

print(shark)
print(s)
print(d)
print(z)

shark.sort(key= lambda x: (x[0], x[1]))


print(shark)

def fun():

    get = 0
    #사냥꾼이 1칸씩 이동할떄
    for i in range(r):
        
        close_shark = 0

        #낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다.
        for j in range(m):
            if shark[j][0] == i:
                now = shark[j][0]
                close_shark = max(now, close_shark)

        for j in range(m):
            if close_shark == shark[j][0]:
                get += z[j]
                #상어 사라지기 

        #상어가 이동한다.
        for j in range(m):
            x, y = shark[j]

            for k in range(1,5):
                
                if d[k] == 1: #위
                    shark[j][1] = shark[j][1] + d[j]
                    if shark[j][1] > c:
                        shark[j][1] = shark[j][1] + (shark[j][1] - c)
                if d[k] == 2: #아래
                    shark[j][1] = shark[j][1] - d[j]
                    if shark[j][1] < 0:
                        shark[j][1] = shark[j][1] - (shark[j][1] - c)
                if d[k] == 3: #오른쪽
                    shark[j][0] = shark[j][1] + d[j]
                    if shark[j][0] > r:
                        shark[j][0] = shark[j][0] - (shark[j][0] - r)
                if d[k] == 4: #왼쪽
                    shark[j][0] = shark[j][1] - d[j]
                    if shark[j][0] < 0:
                        shark[j][0] = shark[j][0] - (shark[j][0] - r)

        #상어가 겹치면, 크기가 큰 상어가 남고, 작은 상어는 다 사라짐


    return
