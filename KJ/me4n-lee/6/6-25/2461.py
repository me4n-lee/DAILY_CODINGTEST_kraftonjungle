# https://www.acmicpc.net/problem/2461
# 대표 선수
# 2461

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

print(graph)

def fun():
    