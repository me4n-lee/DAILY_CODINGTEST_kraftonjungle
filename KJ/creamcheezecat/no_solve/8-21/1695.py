""" 
https://www.acmicpc.net/problem/1695
팰린드롬 만들기
1695
"""

# LCS 참고

import sys
input = sys.stdin.readline

N = int(input())
seq_list = list(map(int,input().split()))

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1,N+1):
    for j in range(1, N+1):
        if seq_list[-i] == seq_list[j-1]:
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            
print(N - dp[-1][-1])