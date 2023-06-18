# https://www.acmicpc.net/problem/10816
# 숫자 카드
# 10816

import sys
input = sys.stdin.readline

n = int(input())

n_list = list(map(int, input().split()))

m = int(input())

# n_list = []
# for _ in range(len(n_list)):

m_list = list(map(int, input().split()))

# print(n_list)
# print(m_list)

n_list.sort()

print(n_list)

dp = [0] * m

def fun():

    for j in range(m):
        
        num = m_list[j]
        start = 0
        end = n

        if n_list[start] == num:
            dp[j] += 1

        if n_list[end-1] == num:
            dp[j] += 1

        while start <= end:
            mid = (start + end) // 2
            now = n_list[mid]
                
            if now >= num:    
                end = mid - 1
                if now == num:
                    dp[j] += 1

            else:
                start = mid + 1

    return dp
            
result = fun()
print(result)

for i in range(len(result)):
    print(result[i], end= " ")