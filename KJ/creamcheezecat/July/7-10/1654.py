""" 
https://www.acmicpc.net/problem/1654<br/>
랜선 자르기<br/>
1654
"""

import sys
input = sys.stdin.readline

K,N = map(int,input().split())

lines = []

for i in range(K):
    num = int(input())
    lines.append(num)
  
lines.sort()

l = 1
r = lines[K-1]
sol = 0

while(l <= r):
    mid = (l + r)//2
    linesum = 0
    
    for line in lines:
        linesum += line//mid
    
    if linesum >= N:
        sol = max(sol,mid)
        l = mid +1
    else:
        r = mid -1  

print(sol)
# print(lines)
