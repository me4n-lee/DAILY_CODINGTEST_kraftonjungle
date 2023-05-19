# https://www.acmicpc.net/problem/20922
# 겹치는 건 싫어
# 20922

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
n_list = list(map(int, input().split()))

# print(n_list)

def fun(n_list):

    result = []

    for i in range(n):

        cnt = 0
        for j in range(i):
            if n_list[i] == n_list[j]:
            # result.append(n_list[i])
                cnt += 1

        
        result.append(cnt)

    for i in range(n):
        if result[i] < k:
            result[i] = 0
        else:
            result[i] = 1

        # else:
        #     result.append()

    return result

answer = fun(n_list)
answer_last = ''.join(map(str, answer))
final = [len(part) for part in answer_last.split('1')]

print(max(final))

