# 배열 두배 만들기

number = [1,2,3,4,5]
answer = []
for i in number:
    answer.append(i*2)
print(answer)

# 각 자리수의 합 구하기 
n= 12345
answer = 0
string= str(n)
for i in string:
    answer +=int(i)
print(answer)   