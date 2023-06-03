# https://www.acmicpc.net/problem/8980
# 택배
# 8980

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())

m_list = []
for _ in range(m):
    a, b, c = map(int, input().split())
    m_list.append([a,b,c])

print(m_list)

m_list.sort(key = lambda x : (x[1], x[0]))
# m_list.sort(key =  lambda x : x[1])

print(m_list)

def fun():

    truck = 0
    result = 0

    for i in range(m):

        now = i+1

        for j in range(m):

            end = m_list[j][1]
            give_num = m_list[j][2]

            if end == now:
                if truck > give_num:
                    result += give_num
                    truck -= give_num

                else:
                    result += truck
                    truck = 0

        for k in range(m): 

            start = m_list[k][0]
            get_num = m_list[k][2]

            if start == now:
                truck += get_num
                if c <= truck:
                    truck = c

    return truck, result


answer = fun()
print(answer)