""" 
https://www.acmicpc.net/problem/2447<br/>
별 찍기 - 10<br/>
2447
"""

import sys
input = sys.stdin.readline


def fun(n):
    if(n == 1):
        return ['*']
    
    Stars = fun(n//3)
    
    draw = []
    for star in Stars:
        draw.append(star * 3)
    for star in Stars:
        draw.append(star +' '*(n//3)+star)
    for star in Stars:
        draw.append(star * 3)
        
    return draw

N = int(input())
print('\n'.join(fun(N)))
    