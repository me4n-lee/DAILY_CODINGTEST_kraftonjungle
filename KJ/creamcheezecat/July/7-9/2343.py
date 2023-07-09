""" 
https://www.acmicpc.net/problem/2343<br/>
기타레슨<br/>
2343
"""

import sys
input = sys.stdin.readline


n,m = map(int,input().split())
bluelay = list(map(int,input().split()))

l = 0
r = bluelay[-1]
total = 1
sol = 0
while l < r :
    m = (l + r)//2
    
    