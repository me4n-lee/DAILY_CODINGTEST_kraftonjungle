# # https://www.acmicpc.net/problem/1062
# # 가르침
# # 1062

# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# n_list = []
# for _ in range(n):
#     a = list(map(str, input().strip()))
#     n_list.append(a)

# # print(n_list)

# def fun():

#     cnt = 0

#     for i in range(n):

#         # print(len(n_list[i]))

#         in_list = list(set(n_list[i]))

#         # last_cnt = len(in_list) - 5

#         # cnt += last_cnt

#         # if last_cnt <= k:

#         answer_list = []

#         for j in range(len(in_list)):
#             if in_list[j] != 'a' and in_list[j] != 'n' and in_list[j] != 't' and in_list[j] != 'i' and in_list[j] != 'c':
#                 answer_list.append(in_list[j])
                   
#         print(answer_list)



#     return cnt

# result = fun()
# print(result)

################################################

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
n_list = []
for _ in range(n):
    a = list(map(str, input().strip()))
    n_list.append(a)

def count_readable_words():
    def check_word(word, known_alphabets):
        for ch in word:
            if ch not in known_alphabets:
                return False
        return True

    def backtrack(idx, cnt, known_alphabets):
        nonlocal max_count

        if cnt == k:
            count = 0
            for word in n_list:
                if check_word(word, known_alphabets):
                    count += 1
            max_count = max(max_count, count)
            return

        if idx == 26:
            return

        if not visited[idx]:
            visited[idx] = True
            backtrack(idx + 1, cnt + 1, known_alphabets + chr(idx + ord('a')))
            visited[idx] = False

        backtrack(idx + 1, cnt, known_alphabets)

    max_count = 0
    visited = [False] * 26
    essential_chars = ['a', 'n', 't', 'i', 'c']
    for ch in essential_chars:
        visited[ord(ch) - ord('a')] = True
    backtrack(0, len(essential_chars), "".join(essential_chars))
    return max_count

result = count_readable_words()
print(result)
