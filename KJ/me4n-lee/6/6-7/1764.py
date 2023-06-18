# https://www.acmicpc.net/problem/1764
# 듣보잡
# 1764

# import sys
# input = sys.stdin.readline

n, m = map(int, input().split())

n_list = []
for _ in range(n):
    a = input()
    n_list.append(a)

m_list = []
for _ in range(m):
    b = input()
    m_list.append(b)

n_list.sort()
m_list.sort()

# def fun():
    # cnt = 0

    # for i in range(n):
    #     for j in range(i, m):
    #         if n_list[i] == m_list[j]:
    #             cnt +=1
    #             result.append(n_list[i])

    # result = list(n_list & m_list)

    # return result

def fun():

    result = []
    i = j = 0

    while i < n and j < m:
        if n_list[i] < m_list[j]:
            i += 1
        elif n_list[i] > m_list[j]:
            j += 1
        else:  # n_list[i] == m_list[j]
            result.append(n_list[i])
            i += 1
            j += 1

    return result

f_list = fun()
# print(f_list)
print(len(f_list))
for i in range(len(f_list)):
    print(f_list[i])
