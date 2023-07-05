# https://www.acmicpc.net/problem/14921<br/>
# 용액합성하기<br/>
# 1406

import sys
input = sys.stdin.readline

n_list = list(map(str, input().strip()))
m = int(input())

m_list = []
for _ in range(m):
    a = list(map(str, input().split()))
    m_list.append(a)

print(m_list)

def fun():

    stack = []
    wait = []

    for i in range(m):

        if m_list[i][0] == 'L':
            if len(stack) != 0:
                a = stack.pop()
                stack.append(a)
                wait.append(a)

        if m_list[i][0] == 'D':
            if len(wait) != 0:
                b = wait.pop()
                n_list.append(b)

        if m_list[i][0] == 'B':
            if len(n_list) != 0:
                n_list.pop()
                
        if m_list[i][0] == 'P':
            stack.append(m_list[i][1])

    return stack

result = fun()
print(n_list)
print(result)


