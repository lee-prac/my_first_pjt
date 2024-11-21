import string


def get_idx_naive(word):
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        char = word[i]
        for j in range(len(string.ascii_lowercase)):
            lo = string.ascii_lowercase[j]
            if result[j] == -1 and char == lo:
                result[j] = i
    print(' '.join([str(num) for num in result]))
# for문 한개당 빅오표기법으로 N이 하나임

def get_idx(word):
    # point 1. ord
    # point 2. O(n^2) -> O(n)
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        #  ord: 문자(알파벳 대소문자) -> 숫자로 바꿔줌
        #  a -> 97, b -> 98 ...
        idx = ord(word[i]) - 97
        if result[idx] == -1:
            result[idx] = i
    print(' '.join([str(num) for num in result]))


get_idx_naive('baekjoon')
# get_idx('baekjoon')