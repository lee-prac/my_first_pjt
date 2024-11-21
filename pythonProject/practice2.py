# 숙제 - 25
# number = [1, 4, 4, 4, 4, 4, 4]에 중복 제거 해주세요
# number = [1, 4, 4, 4, 4, 4, 4]
# result = []
# for value in number:
#     if value not in result:
#         result.append(value)
# print(result)

# 숙제 - 26
# number = [1, 4, 4, 4, 4, 4, 4, 5]에서 5 제거 후 출력해주세요
# number = [1, 4, 4, 4, 4, 4, 4, 5]
# number.remove(5)
# print(number)

# 숙제 - 27
# number = [1, 2, 3, 4, 5]에서 3 제거 후 나머지 요소의 평균 값 구해주세요
# number = [1, 2, 3, 4, 5]
# number.remove(3)
# for i in number:
#     total = sum(number)/len(number)
# print(total)


# 숙제 - 28
# number = [1, 2, 3, 4, 5]에서 뒤의 3개만 출력해주세요 후 귀차나 슬슬
# number = [1, 2, 3, 4, 5]
# print(number[2:])


# # 숙제 - 29
# # number = [1, 4, 4, 4, 4, 4, 4. 5]에서 중복된 요소의 개수 출력
# number = [1, 4, 4, 4, 4, 4, 4,5]
# cnt = number.count(4)
# print(cnt)


# # 숙제 - 30
# # number = [1, 4, 4, 4, 4, 4, 4. 5]에서 요소 4의 위치(인덱스)를 출력하세요
# number = [1, 4, 4, 4, 4, 4, 4, 5]
# print(number.index(4))

# # 숙제 - 31
# # list_1 = [1, 2, 3]
# # list_2 = [4, 5, 6]
# # 위의 두개의 리스트를 하나로 합쳐주세요
# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# print(list_1 + list_2)

# 숙제 - 32
# number = [[1, 2], [3, 4], [5, 6]]의 모든 요소를 더해주세여
# number = [[1, 2], [3, 4], [5, 6]]
# result = 0
# for i in number:
#     for j in i:
#         result += j
# print(result)


# # 숙제 - 33
# # a = 11
# # b = 22
# # 위의 변수를 선언 후 a의 값을 22, b의 값을 11로 교환
# a = 11
# b = 22
# a, b = b, a
# print(a, b)


# # 숙제 - 34
# # 값 3, 6, 9를 a, b, c 변수들에게 각각 할당해라
# a = 3
# b = 6
# c = 9
# print(a, b, c)



# # 숙제 - 35
# # (44, 33, 22, 11)의 튜플을 리스트로 변환 후 출력
# tp_num = 44, 33, 22, 11
# tp_list = []
# for i in tp_num:
#     tp_list.append(i)
# print(tp_list)


# # 숙제 - 36
# # 리스트 [11, 22, 33, 44]에 11의 값을 110으로 변경
# # 튜플 (11, 22, 33, 44)에 11의 값을 110 변경 시도
# num = [11, 22, 33, 44]
# num[0] = int(110)
# print(num)
#
# tp_num = 11, 22, 33, 44
# tp_list = []
# for i in tp_num:
#     tp_list.append(i)
#     tp_list[0] = int(110)
# tp_num1 = tuple(tp_list)
# print(tp_num1)
# # 리스트 변환 후 값을 바꿔 다시 새로운 튜플로 만들었을 뿐이지 튜플의 값을 바꾼 것은 아님. 파이썬에서 튜플 값을 바꾸는 것은 불가능하다고 함.

# 숙제 - 37
# 리스트 [44, 33, 22, 11]을 튜플로 변환하고, 55를 추가 시도해보아라.
# 안 된다면 그 이유는?
#
# tp_list = [44, 33, 22, 11]
# tp_num = tuple(tp_list)
# var = tp_num.append

# # 숙제 - 40
# # 빈 딕셔너리에 키: name, 값, 본인 이름을 추가하고 출력
#
# my = {}
# my['name'] = '예지'
# print(my)


# 숙제 - 41
# {'name': 'won', 'age': 1000} 에서 키 age의 값을 출력

# user = {'name': 'won', 'age': 1000}
# print(user['age'])


# # 숙제 - 42
# # {'apple': 111, 'banana': 222, 'cherry': 333} 에서 모든 키 출력
#
# fruits = {'apple': 111, 'banana': 222, 'cherry': 333}
# for key in fruits:
#     print(key)


# 숙제 - 43
# # {'apple': 111, 'banana': 222, 'cherry': 'babo'} 에서 모든 값 출력
#
# fruits = {'apple': 111, 'banana': 222, 'cherry': 'babo'}
# print(fruits.values())
#
#
#
# # 숙제 - 44
# # {'apple': 111, 'banana': 222, 'cherry': 'babo'} 에서 값이 babo가 있다면 babo 출력
# fruits = {'apple': 111, 'banana': 222, 'cherry': 'babo'}
# if 'babo' in fruits.values():
#     print('babo')
#


# # 숙제 - 45
# # {'apple': 111, 'banana': 222, 'cherry': 'babo'} 에서 apple 삭제 후 출력
# fruits = {'apple': 111, 'banana': 222, 'cherry': 'babo'}
# del fruits['apple']
# print(fruits)


# # 숙제 - 46
# # {'apple': 111, 'banana': 222, 'cherry': 'babo'} 에서 banana의 값을 babooo로 수정
#
# fruits = {'apple': 111, 'banana': 222, 'cherry': 'babo'}
# fruits['banana'] = 'babooo'
# print(fruits)


# # 숙제 - 47
# # {'a': 1, 'b': 2}와 {'c': 3, 'd': 4}를 합치시오,
# dic1 = {'a': 1, 'b': 2}
# dic2 = {'c': 3, 'd': 4}
# dic1.update(dic2)
# print(dic1)


# 숙제 - 48
# {'apple': 111, 'banana': 222, 'cherry': 'babo'}에서 모든 키와 모든 값을 순회하여 출력

# fruits = {'apple': 111, 'banana': 222, 'cherry': 'babo'}
# for key,value in fruits.items():
#     print(key,value)



# # 숙제 - 49
# 			# {'apple': 111, 'banana': 222, 'cherry': 'babo'} 키 'cherry'의 '값'을 출력 하시오
# # 없을 경우 None이라고 출력
#
# fruits = {'apple': 111, 'banana': 222, 'cherry': 'babo'}
# if 'cherry' in fruits:
#     print(fruits['cherry'])
# else:
#     print(None)


# # 숙제 - 50
# # {'apple': 111, 'banana': 222, 'cherry': 'babo'} 의 길이 출력
#
# fruits = {'apple': 111, 'banana': 222, 'cherry': 'babo'}
# print(len(fruits))


# # 숙제 - 51
# # {'apple': 111, 'banana': '222', 'cherry': True} 값의 자료형 출력
# #
# fruits = {'apple': 111, 'banana': '222', 'cherry': True}
# for key,value in fruits.items():
#     print(type(value))


# 숙제 - 52
# {'apple': 111, 'banana': '222', 'cherry': 333} 에 값을 합산하라
# hint 형변환
#
fruits = {'apple': 111, 'banana': '222', 'cherry': 333}
fruit = sum(fruits)
print(fruit)

# # 숙제 - 53
# # 문자열 "abcd abcd babo'에서 각 문자에 개수를 딕셔너리에 저장 후 출력
# # 출력 시 -> {'a': 3, 'b': 4, 'c': 2, 'd': 2, ' ': 2, 'o': 1}
#
# text = 'abcd abcd babo'
# count = {}
#
# for char in text:
#     if not char.isalpha():
#         continue
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1
# print(count)



