# https://www.acmicpc.net/problem/10974
# 모든 순열
# 10974

import sys
input = sys.stdin.readline
from itertools import permutations

n=int(input())
n_list=[]

for i in range(1,n+1):
    n_list.append(i)

result = list(permutations(n_list, n))

for i in result:
    for j in i:
        print(j, end = " ")
    print()
