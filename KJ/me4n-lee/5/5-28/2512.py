# https://www.acmicpc.net/problem/2512
# 예산
# 2512

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())

# print(n_list)

def fun():

    result = 0
    cnt = 0

    start = 1
    end = max(n_list)
    
    while start <= end:
        mid = (start + end) // 2
        sum_money = 0

        for i in range(n):

            if n_list[i] >= mid:
                sum_money += mid
            
            else: 
                sum_money += n_list[i]
        
        # print(cnt)

        if sum_money <= m:
            result = mid
            start = mid + 1

        else:
            end = mid -1

    return result

answer = fun()
print(answer)