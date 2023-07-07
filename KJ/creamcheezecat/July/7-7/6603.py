""" 
https://www.acmicpc.net/problem/6603<br/>
로또<br/>
6603
"""

from itertools import combinations
import sys
input = sys.stdin.readline

def fun(arr):
    ncount = len(arr)
    result = [0] * 6
    for combination in combinations(arr, 6):
        result[:6] = combination

        # 조합 출력
        print(*result)


while(1):
    tc = list(map(int,input().split()))
    if tc[0]== 0:
        break
    del tc[0]
    
    fun(tc)
    print()
    
    
#print(tc)

