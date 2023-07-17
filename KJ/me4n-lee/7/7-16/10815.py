# https://www.acmicpc.net/problem/10815
# 숫자 카
# 10815

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

# print(n_list)
# print(m_list)

def fun():

    answer = []

    for i in range(m):

        result = 0

        now = m_list[i]

        start = 0
        end = n - 1

        while start <= end:
            mid = (start + end) // 2

            if n_list[mid] < now:
                start = mid + 1

            elif n_list[mid] > now:
                end = mid - 1

            else:
                result = 1
                break
        
        answer.append(result)

    return answer

final = fun()
for i in range(m):
    print(final[i], end = " ")
        