# https://www.acmicpc.net/problem/5430
# AC
# 5430

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def fun(fun_list, n_list):
    
    r_list = deque(n_list)

    for i in range(len(fun_list)):
        
        if len(r_list) == 0:
            return 'error'

        if fun_list[i] == 'R':
            r_list.reverse()
        # else:
        #     if len(n_list) == 0:
        #         return 'error'       
        #     else:
        #         r_list.popleft()

        else:
            if not r_list:
                return 'error'
            
            r_list.popleft()


    return list(r_list)

for _ in range(t):
    fun_list = list(map(str, input().strip()))
    n = int(input())
    n_list = input().replace('[', '').replace(']', '').strip().split(',')

    answer = fun(fun_list, n_list)

    if answer == 'error':
        print('error')
    else:
        print('[', end ='')
        for i in range(len(answer)):
            if i == 0:
                print(answer[i], end ='')
            else:
                print(',' + answer[i], end ='')
        print(']')
    