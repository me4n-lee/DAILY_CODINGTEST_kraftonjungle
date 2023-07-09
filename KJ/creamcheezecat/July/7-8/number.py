""" 
https://www.acmicpc.net/problem/10815<br/>
숫자카드<br/>
10815
"""

import sys
input = sys.stdin.readline

N = int(input())
n_list = list(map(int,input().split()))
M = int(input())
m_list = list(map(int,input().split()))

# print(n_list)
# print(m_list)

n_list.sort()

for i in range(M):
    left = 0
    right = N-1 
    found = 0
    while left <= right:
        mid = (left+right)//2
        if n_list[mid] == m_list[i]:
            found = 1
            break
        elif n_list[mid] > m_list[i]:
            right = mid - 1
        else:
            left = mid + 1
            
    m_list[i] = found
    
            
print(*m_list)