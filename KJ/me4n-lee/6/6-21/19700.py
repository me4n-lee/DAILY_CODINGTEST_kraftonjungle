# https://www.acmicpc.net/problem/19700
# 수업
# 19700

import sys
input = sys.stdin.readline

n = int(input())

stu = []
for _ in range(n):
    h, k = map(int, input().split())
    stu.append([h, k])

print(stu)

stu.sort(key= lambda x : x[0], reverse= True)

print(stu)

def fun():

    # while stu == 0:
    #     if
    #     height = stu[i][0]
    #     man = stu[i][1]

    answer = 0

    for i in range(n):

        cur_h, cur_k = stu[i]
    
        for j in range(i+1, n):


                answer += 1
                

    return answer

result = fun()
print(result)