# def count_passer(score, c):
#     answer = 0
#
#     return answer
#
#
# # [80, 40, 90, 55, 94, 30, 60, 44]
# print(count_passer([80, 40, 90, 55, 94, 30, 60, 44], 60))
# print(count_passer([20, 50, 20, 80, 45], 30))



#
# def remove_duplicates(d_list):
#     result = set[duplicated_list]
#     for value in d_list:
#         return result
# duplicated_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
# print(set(duplicated_list))
#
# #
# 스택 문제 1
# 키보드 Backspace 기능 구현
# input_string = ‘123//45/6789///’
# /를 만나면 앞의 값을 삭제
# 참고 - 맨앞에 /만나면 어떻게 처리해야 되는지 생각 해보기
# answer = ‘146’
# 8:45
# def backspace_string(input_string):
#     stack = []
#
#     return answer
#
# print(backspace_string("123//45/6789///"))
#
#
#
# # 스택 문제 2
# # 괄호 문법 검사기
# # bracket1: [[[[]]]][] → answer ‘YES’
# # bracket2: [[[[[[[[[[[[[[[[]] → answer ‘NO’
# def is_bracket(b):
#     answer = "YES"
#     for :
#         return answer
#
#
# # [[[[]]]][]
# # [[[[[[[[[[[[[[[[]]
#
# # YES
# print(is_bracket("[[[[]]]][]"))
#
# # No
# print(is_bracket("[[[[[[[[[[[[[[[[]]"))



# N개의 단위로 아래와 같이 리스트로 출력(함수)
# 결과: [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R'], ['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z']]
#
# alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
#                  'U', 'V', 'W', 'X', 'Y', 'Z']

# def split_n_list(split_size=3):
#     answer = []
#     for import split(split_size[for i range(3)]):
#     return answer
#
#
# print(f"결과: {split_n_list()}")






# [숙제] - 07.18
# 기본 문제 1)
# # 딕셔너리 구조에서 Value 값이 25 이상 필터링 후 출력
# d = {'a': 25, 'b': 2, 'c': 45, 'd': 21, 'e': 44, 'f': 99}
#     8:32
# [숙제] - 07.18
# 기본 문제 2)
# 딕셔너리를 활용하여 아래와 같이 출력해주세요
# key "one" has values [1, 2, 3, 4, 5, 6, 7, 8, 9] -> total : 9 key "two" has values [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33] -> total : 23 key "three" has values [44, 45, 46, 47, 48] -> total : 5
#
#
#

# 버블 정렬 구현 코드
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr





# # 구구단
# for i in range(2, 10):
#     print(f'외부 루프{i}'),
#     for  j in range(1, 10):
#         print(f'내부 루프 {j}')
#         print(f'{i} x {j} = {i * j}')

