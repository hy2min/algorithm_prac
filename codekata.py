# # 배열 두배 만들기

# number = [1,2,3,4,5]
# answer = []
# for i in number:
#     answer.append(i*2)
# print(answer)

# # 각 자리수의 합 구하기
# n= 12345
# answer = 0
# string= str(n)
# for i in string:
#     answer +=int(i)
# print(answer)

# # 세균 증식
# # n=처음 세균 수
# # t=경과한 시간
# n=50
# t=4
# answer = n*(2**t)
# print(answer)

# # 삼각형의 완성조건
# sides = [6,5,13]
# sides.sort()
# if sides[2] < sides[0] + sides[1] :
#     answer = 1
# else :
#     answer = 2
# print(answer)

# # 중앙값 구하기
# # 리스트를 오름차순으로 정렬 후 중간값을 구함
# array = [3,7,-5,-1,10]
# array.sort()
# answer = array[len(array)//2]
# print(answer)

# # 짝수는 싫어요
# n=14
# answer = []
# for i in range(n+1) :
#     if i % 2 ==1:
#         answer.append(i)
# print(answer)

# # 순서쌍의 개수
# n=4
# answer = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         answer += 1
# print(answer)

# # 모음 제거
# # 문자열에서 a,e,i,o,u를 제거하여 남은 문자를 표시
# my_string = "mice to meet you"
# vowel = ["a","e","i","o","u"]
# for i in vowel:
#     if i in my_string:
#         answer = my_string.replace(i,'')
# print(answer)

# # 문자 반복 출력하기
# my_string = "hello"
# n = 3
# answer = ""
# for i in range(len(my_string)):
#     answer += my_string[i]*n
# print(answer)

# # 옷가게 할인 받기
# price = 150000
# if price >= 500000 :
#     answer = price * 0.8
# elif price >= 300000 :
#     answer = price * 0.9
# elif price >= 100000 :
#     answer = price * 0.95
# else :
#     answer = price
# print(int(answer))

# # 제곱수 판별하기
# n=145
# answer = 2
# for i in range(1,n+1):
#     if n / i == i :
#         answer = 1
#         break
# print(answer)

# # 숨어있는 숫자의 덧셈
# my_string ="aAb1B2cC34oOp"
# answer = 0
# for i in my_string :
#     if i.isdigit() == True :
#         answer += int(i)
# print(answer)

# # 정수 부분
# flo= 69.32
# answer = int(flo)
# print(answer)

# # n의 배수
# num=98
# n=2
# if num % n ==0 :
#     answer = 1
# else :
#     answer = 0
# print(answer)

# # 문자열의 앞의 n글자
# my_string = "He110W0r1d"
# n = 5
# answer = my_string[:n]
# print(answer)

# # 이어 붙인 수
# num_list = [5,7,8,3]
# odd = ''
# even = ''
# for i in num_list :
#     if i % 2 == 1 :
#         odd += str(i)
#     else :
#         even += str(i)
# answer = int(odd) + int(even)
# print(answer)

# # flag에 따라 다른 값 반환하기
# a = -4
# b = 7
# flag = False
# if flag == True :
#     answer = a+b
# elif flag == False :
#     answer = a-b
# print(answer)

# # 배열의 원소 삭제하기
# arr = [293,1000,395, 678]
# delete_list = [94,777,104,1000,112]
# answer = []
# for i in arr:
#     if i  not in delete_list :
#         answer.append(i)
# print(answer)

# # 꼬리 문자열
# str_list = ["abc","def","ghi"]
# ex = "ef"
# answer = ""
# for i in str_list :
#     if ex  not in i :
#         answer += i
# print(answer)

# # 문자열 정수의 합
# num_str = "123456789"
# answer = 0
# for i in num_str :
#     answer += int(i)
# print(answer)

# # x사이의 개수
# myString = "xabcxdefxghi"
# answer = []
# for i in myString.split('x') :
#     answer.append(i.count(str())-1)
# print(answer)

# # ad 제거하기
# strArr = ["and","notad","abcd"]
# answer = []
# for i in strArr :
#     if "ad" not in i :
#         answer.append(i)
# print(answer)

# # 홀수 vs 짝수
# num_list = [4,2,6,1,7,6]
# answer = max(sum(num_list[::2]),sum(num_list[1::2]))
# print(answer)

# # 가장 큰 수 찾기
# array = [9,10,11,8]
# for i in range(len(array)) :
#     if array[i] == max(array) :
#         answer = [max(array), i]
# print(answer)

# # 0 떼기
# n_str = "854020"
# for i,num in enumerate(n_str) :
#     if num != "0" :
#         answer = n_str[i:]
#         break
# print(answer)

# # I로 만들기
# myString = "abcdevwxyz"
# l_before = "abcdefghijk"
# for str in myString :
#     if str in l_before :
#         myString = myString.replace(str, "l")
# print(myString)

# # 가까운 1 찾기
# arr = [1,1,1,1,0]
# idx = 3
# answer = 0
# for i in range(idx, len(arr)) :
#     if arr[i] == 1 :
#         answer = i
#         break
#     else :
#         answer = -1
# print(answer)

# # 최댓값 만들기(2)
# numbers = [10, 20, 30, 5, 5, 20, 5]
# numbers.sort()
# answer = float('-inf')
# for i in range(len(numbers)-1) :
#     answer = max(answer,numbers[i]*numbers[i+1])
# print(answer)

# # 주사위의 개수
# box = [10,8,6]
# n = 3
# answer = (box[0]//n) * (box[1]//n) * (box[2]//n)
# print(answer)

# # 직각삼감형 출력하기
# n = int(input())
# for i in range(1,n+1) :
#     print('*'* i)

# # 특별한 이차원 배열 2
# arr = [[19, 498, 258, 587], [63, 93, 7, 754],[258, 7, 1000, 723], [587, 754, 723, 81]]
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[i][j] == arr[j][i]:
#             answer = 1
#         else :
#             answer = 0
#             break
#     if answer ==0 :
#         break
# print(answer)

# # 문자열 정렬하기 (1)
# my_string = "p2o4i8gj2"
# answer = []
# for i in my_string :
#     if i.isdigit() == True :
#         answer.append(int(i))
# answer.sort()
# print(answer)

# # 인덱스 바꾸기
# my_string = 'hello'
# num1 = 1
# num2 = 2
# str_list = list(my_string)
# str_list[num1], str_list[num2] = str_list[num2], str_list[num1]
# answer = ''.join(str_list)
# print(answer)

# # 콜라츠 수열 만들기
# n = 10
# answer = []
# while n != 1 :
#     if n % 2 ==0 :
#         n = n // 2
#     else :
#         n = 3*n + 1
#     answer.append(n)
# print(a)

# # 특별한 이차원 배열1
# n = 3
# answer = [[0 for i in range(n)] for j in range(n)]
# for i in range(n) :
#     for j in range(n) :
#         if i == j :
#             answer[i][j] = 1
# print(answer)

# # 문자 리스트를 문자열로 변환하기
# arr = ['a', 'b', 'c']
# answer = ''
# for i in arr:
#     answer+=(i)
# print(answer)

# # 배열 만들기3
# arr = [1,2,3,4,5]
# intervals = [[1,3],[0,4]]
# answer = []
# for i in intervals :
#     answer+=arr[i[0]:i[1]+1]
# print(answer)

# # 간단한 식 계산하기
# binomial = '43 + 12'
# answer = 0
# binomial = binomial.split()
# if binomial[1] == '+' :
#     answer = int(binomial[0]) + int(binomial[2])
# elif binomial[1] == '-' :
#     answer = int(binomial[0]) - int(binomial[2])
# elif binomial[1] == '*' :
#     answer = int(binomial[0]) * int(binomial[2])
# print(answer)

# # 접미사 배열
# my_string = 'programmers'
# answer = []
# for i in range(len(my_string)) :
#     answer.append(my_string[i:])
#     answer.sort()
# print(answer)

# # 약수 구하기
# n = 24
# answer = []
# for i in range(1,n+1) :
#     if n % i == 0 :
#         answer.append(i)
# print(answer)

# # 덧셈식 출력하기
# a,b = map(int,input().split())
# print(f'{a} + {b} = {a+b}')

# # 배열 회전시키기
# from collections import deque
# numbers = [1,2,3]
# direction = 'right'
# answer = deque(numbers)
# if direction == 'right' :
#     answer.appendleft(answer.pop())
# elif direction == 'left' :
#     answer.append(answer.popleft())
# print(list(answer))

# # 수 조작하기 2
# reverse = {
#     +1 : 'w',
#     -1 : 's',
#     +10 : 'd',
#     -10 : 'a'
# }

# numLog = [0,1,0,10,0,1,0,10,0,-1,-2,-1]
# answer = ''
# for i in range(1,len(numLog)) :
#     answer += reverse[numLog[i]-numLog[i-1]]
# print(answer)

# # 문자열 돌리기
# str = input()
# for i in str :
#     print(i)

# # 외계행성의 나이
# from string import ascii_lowercase
# age = 23
# alp_list = list(ascii_lowercase)[:10]
# answer = ''
# chg_age = str(age)
# for i in chg_age :
#     answer += alp_list[int(i)]
# print(answer)

# # 문자열 잘라서 정렬하기
# myString = "axbxcxdx"
# answer = []
# answer = myString.split('x')
# answer = [s for s in answer if s] 
# answer.sort()
# print(answer)

# # 숫자 찾기
# num = 29183
# k = 1
# answer = 0
# for i, n in enumerate(str(num)) :
#     if int(n) == k :
#         answer = i+1
#         break
#     else :
#         answer = -1
# print(answer)

# # 9로 나눈 나머지
# number = "123"
# cnt = 0
# answer = 0
# for i in number :
#     cnt += int(i)
# answer = cnt % 9
# print(answer)    

# 주사위 게임 2
a = 1
b = 2
c = 1
answer = 0
if a != b and b != c and c != a :
    answer = a + b + c
elif a == b and b == c and c == a :
    answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
else :
    answer = (a+b+c)*(a**2+b**2+c**2)
print(answer)