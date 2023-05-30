# https://www.acmicpc.net/problem/2170
# 선 긋기
# 2170

import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    x, y = map(int, input().split())
    graph.append([x,y])

# print(graph)

graph.sort(key = lambda x: x[0])




#### dp 풀이 ####
# # print(graph)
# max_graph = max(max(graph))

# dp = [0] * (max_graph + 1)

# def fun():

#     start = 0
#     end = 0

#     for i in range(n):
#         start = graph[i][0]
#         end = graph[i][1]

#         for j in range(start, end):
            
#             if dp[j] == 0:
#                 dp[j] = 1

#     return dp

# sum = 0

# for i in range(n):
#     sum += graph[i][1] - graph[i][0]

# # print(sum) 


#### 완탐 풀이 실패 ####
# def fun():

#     sum_same = 0

#     for i in range(n):
#         start = graph[i][0]
#         end = graph[i][1]

#         for j in range(i, n):
#             n_start = graph[j][0]
#             n_end = graph[j][1]

#             if end > n_start:

#                 if end > n_end:
#                     sum_same += n_end - n_start
                
#                 else:
#                     sum_same += end - n_start


#     return sum_same

def fun():

    total_length = 0

    start = graph[0][0]
    end = graph[0][1]

    for i in range(1, n):
        if graph[i][0] <= end:
            end = max(end, graph[i][1])

        else:
            total_length += end - start
            start = graph[i][0]
            end = graph[i][1]

    total_length += end - start

    return total_length

result = fun()
print(result)
