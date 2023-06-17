# https://www.acmicpc.net/problem/2011
# 암호 코드
# 2011

import sys
input = sys.stdin.readline

n_list = list(map(int, input().strip()))

print(n_list)

n = len(n_list)

dp = [0] * n
visit = [0] * n

def fun():

    cnt = 0

    # for i in range(n):

    #     if i == n:
    #         dp[i] = 0
    #     else:
    #         if n_list[i] == 1 or n_list[i] == 2:
    #             dp[i] += 1
    #             if n_list[i+1] == 1 or n_list[i+1] == 2:
    #                 dp[i] += 1
    #         else:
    #             dp[i] = 0
    if n_list[0] == 1 or 2:
        dp[0] = 2
    else: 
        dp[0] = 1

    for i in range(1, n):
        if n_list[i] == 1 or n_list[i] == 2:
            if n_list[i-1] == 1 or n_list[i-1] == 2:
                if visit[i-1] == 1:
                    dp[i] = dp[i-1] * 2
                    cnt += 1
                else:
                    dp[i] = dp[i-1] + 2
                    visit[i] = 1
            
            else:
                dp[i] = dp[i-1] * 2
        
        else:
            dp[i] = dp[i-1]

    print(visit)            

    answer = dp[-1] - cnt

    return answer


result = fun()

print(result)
