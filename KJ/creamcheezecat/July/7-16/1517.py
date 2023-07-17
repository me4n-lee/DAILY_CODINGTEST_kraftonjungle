""" 
https://www.acmicpc.net/problem/1517<br/>
버틀 소트<br/>
1517
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
testcase = list(map(int,input().split()))
sol = 0

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    global sol
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] <= high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
            sol += len(low_arr)-l
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


res = merge_sort(testcase)

print(sol)

