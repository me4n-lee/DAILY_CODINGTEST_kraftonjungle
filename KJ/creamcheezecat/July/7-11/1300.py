""" 
https://www.acmicpc.net/problem/1300<br/>
K번째 수<br/>
1300
"""

import sys
input = sys.stdin.readline

N = int(input()) # 이중 배열 크기
k = int(input()) # 일차원 배열 인덱스

l = 1
r = N*N
sol = 0
while l <= r:
    mid = (l+r)//2
    cnt = 0
    for i in range(1,N+1):
        cnt += min(N,mid // i)
        
    if cnt >= k:
        sol = mid
        r = mid -1
    else:        
        l = mid +1
    
print(sol)