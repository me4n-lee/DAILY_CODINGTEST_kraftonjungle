# https://www.acmicpc.net/problem/1759
# 암호 만들기
# 1759

import sys
input = sys.stdin.readline

l, c = map(int, input().split())
c_list = list(map(str, input().split()))

print(c_list)

c_list.sort()

print(c_list)

copy_list = c_list.copy()

print(copy_list)

def fun():

    for i in range(c-1, 0, -1):
        for j in range(c-2, 0, -1):

            copy_list = c_list.copy()
            copy_list.remove(copy_list[i])
            copy_list.remove(copy_list[j])

            m_count = 0
            j_count = 0

            print(copy_list)

    for k in range(len(copy_list)):

        if copy_list[k] == 'a' and copy_list[k] == 'e' and copy_list[k] == 'i' and copy_list[k] == 'o' and copy_list[k] == 'u':
            m_count += 1
        else:
            j_count += 1

        if m_count >= 1 and j_count >= 2:
            print(copy_list)
            

result = fun()