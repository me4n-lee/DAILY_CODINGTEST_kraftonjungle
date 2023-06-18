# https://www.acmicpc.net/problem/13335
# 트럭
# 13335

import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())
n_list = list(map(int, input().split()))

def fun():

    sum = 1
    cnt = 0
    truck_sum = 0
    for i in range(n):
        if i == 0:
           sum += w 
        else:
            if n_list[i] +n_list[i-1] <= l:
                sum += w
                cnt += 1
            else:
                sum += w

    sum = sum - cnt

    return sum

result = fun()
print(result)