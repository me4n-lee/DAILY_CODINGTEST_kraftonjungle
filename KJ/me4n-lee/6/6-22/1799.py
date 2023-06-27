# https://www.acmicpc.net/problem/1799
# 비숍
# 1799

import sys
input = sys.stdin.readline

n = int(input())

n_list = []
for _ in range(n):
    a = list(map(int, input().split()))
    n_list.append(a)

# print(n_list)

visit = [[0] * n for _ in range(n)]

print(visit)

def fun():

    max_num = 0
    # stack = []
    
    cnt = 0

    for i in range(n):
        for j in range(n):
            

            if n_list[i][j] == 1:
                
                cnt += 1
                for k in range(n):
                    
                    if i+k <= 4 and j+k <= 4:
                        n_list[i+k][j+k] = 0

                    if i-k >=0 and j+k <= 4:
                        n_list[i-k][j+k] = 0

                    if j-k >=0 and i+k <= 4:
                        n_list[i+k][j-k] = 0

                    if i-k >=0 and j-k >=0:
                        n_list[i-k][j-k] = 0


            visit[i][j] = cnt

    
    print(visit)


    return cnt

result = fun()
print(result)