# #피라미드
# n = 5
# for i in range(1, n+1): # 별 지정
#     n += 1
#     print('*', end='')
#     # for j in range(i + 1): # 여백 지정
#     #     print(' ', end='')#별 + 여백 출력
#     print()# 빈줄 출력



# [숙제] - 07.19
# 구구단
# 출력for
# for i in range(2, 10):# i를 증가시키는 반복문
#     for j in range(1, 10):# j를 증가시키는 반복문 정의
#         print(f'{i} x {j} = {i*j}')# 구구단 결과 출력 /i*j로 결과 출력
#     print()

# [숙제] - 07.19
# 각 엘리먼트를 다 더해주세요
# 예시 입력 값: a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 출력 값: 45
# 참고) 각 요소 다 더하기(1 + 2 + 3 + 4....)

# 주석 다는 중입니다..ㅠㅠ 나중에 수정할게여
# a = [[1,2,3], [4,5,6], [7,8,9]]# 리스트 지정
# result = 0
# for i in a: # i에 리스트 a를 할당하여 돌아가면서 집어넣음.
#     for j in i: # j에 리스트 i를 할당하여 집어넣음
#         result += j # result에 j를 전부 더한 값을 추가함
# print(result) # 덧셈 결과 출력

# 두 개의 리스트의 모든 요소를 덧셈 후 결과를 출력해주세여
# 입력 값
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# 참고) - 1+4, 1+5, 1+6, 2+4……
# 결과 값
# 5 6 7 6 7 8 7 8 9




list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = []
for i in list1:
    for j in list2:
        result.append(i+j)#i에 더한 값을 추가함
print(result)

# def recursive_func_1(n):
#     if n == 0:
#         return
#     else:
#         recursive_func_1(n-1)
#         print(n, end=' ')
#
#
# recursive_func_1(5)




# [숙제] - 07.22
# 피보나치 수열을 구현
# 재귀함수
# 코드 흐름에 대해 알려주세요
# 이미지도 오케



# 이 함수를 재귀함수로 바꿔보시오
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# print(gcd(60, 48))
#
# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return b, a % b
# gcd(60, 48)




def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# 예제 사용
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci(i)}")