# 점프투파이썬 171page

# 파일 읽고 쓰기

# f = open('새파일.txt', 'w')  # 파일 객체 = open(파일명, 파일 열기 모드)
# f.close()
# r : 읽기 모드, 파일을 읽기만 할 때 사용
# w : 쓰기 모드, 파일에 내용을 쓸 때 사용
# a : 추가 모드, 파일의 마지막에 새로운 내용을 추가할 때 사용
# x : 베타적 생성을 위해 열리고 이미 존재하는 경우 실패
# b : 2진 바이너리 모드
# t : 텍스트 모드(기본값)
# + : 업데이트(읽기 쓰기)를 위한 디스크 파일 열기

# 파일 절대경로 생성
# f = open('D:/PythonExam/Files/새파일txt', 'w')  # 디렉토리가 없으면 생성되지 않음
# f.close()
# f = open('D:/PythonExam/새파일2.txt', 'w')
# f.close()

# 파일 상대경로 생성
# f = open('./새파일3.txt', 'w')  # ../ : 상위경로, ./ : 현재경로
# f.close()

# 파일을 쓰기 모드로 열어 출력값 적기
# f = open('새파일.txt', 'w')
# for i in range(1, 11):
#     data = '%d번 줄입니다.\n' %i
#     f.write(data)
# f.close()

# 인코딩 에러 발생시 * 파이썬은 기본적으로 'cp949' 인코딩 방식을 사용하고 있는것 같다. 
# https://suwoni-codelab.com/python%20%EA%B8%B0%EB%B3%B8/2018/03/12/Python-Basic-file/ 참고
# f = open('새파일.txt', 'w', 1, 'utf-8')
# for i in range(1, 11):
#     data = '%d번 줄입니다.\n' %i
#     f.write(data)
# f.close()

# 프로그램 외부에 저장된 파일 읽는 방법
# f = open('새파일.txt', 'r')
# line = f.readline()
# print(line)
# f.close()

# 인코딩 에러 발생시
# f = open('새파일.txt', 'r', 1, 'utf-8')
# line = f.readline()
# print(line)
# f.close()

# 파일 읽기2
# f = open('새파일.txt', 'r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# 파일읽기3
# f = open('새파일.txt', 'r')
# data = f.read()
# f.close()
# print(data)

# 파일에 새로운 내용 추가
# f = open('새파일.txt', 'a')
# for i in range(11, 20):
#     data = '%d번째 줄 입니다.\n' %i
#     f.write(data)
# f.close()

# f = open('새파일.txt', 'w')  # 'w' 모드로 열기만 해도 파일의 기존 내용이 다 사라지니 주의
# f.write('Hi This is test msg')
# f.close()

# with 문과 함께 쓰는 파일 입출력
# with open('새파일.txt', 'a') as f:
#     f.write('Life is too short. You need python\n')  # with 문을 빠져나가면 자동으로 close 됨

# sys 모듈로 프로그램 매개변수 주기
# import sys

# args = sys.argv[1:]
# for i in args:
#     print(i)
# 입력 받은 인수를 for문을 사용해 하나씩 출력 하겠다는 의미
# cmd로 현재 경로에서 python 20191213.py aaa bbb ccc 라고 매개변수를 주어 실행하면
# aaa
# bbb
# ccc
# 라고 출력 됨

# sys 모듈로 프로그램 매개변수 주기2
# import sys

# args = sys.argv[1:]
# for i in args:
#     print(i.upper(), end=' ')

# ================================================================================================
# 연습문제 179page

# 1. 홀짝 판별 함수
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

def is_odd2(number):
    return number % 2 == 1

print(is_odd(4))
print(is_odd2(4))
print('=' * 50)

# 2. 입력으로 들어오는 모든 수의 평균
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)
print(avg_numbers(1, 2))
print(avg_numbers(1, 2, 3, 4, 5))
print('=' * 50)

# 3. 프로그램 오류 수정
# input1 = input('첫번쨔 숫자를 입력 하세요 : ')
# input2 = input('두번째 숫자를 입력 하세요 : ')
# # total = input1 + input2
# print(total)
# 위 코드를 올바르게
# input1 = input('첫번쨔 숫자를 입력 하세요 : ')
# input2 = input('두번째 숫자를 입력 하세요 : ')
# total = int(input1) + int(input2)
# print(total)
print('=' * 50)

# 4. 결과가 다른 하나
print('you' 'need' 'python')
print('you' + 'need' + 'python')
print('you', 'need', 'python')
print(''.join(['you', 'need', 'python']))
print('=' * 50)

# 5. 파일 읽기 쓰기
# f1 = open('test.txt', 'w')
# f1.write('Life is too short')

# f2 = open('test.txt', 'r')
# print(f2.read())

# 위 코드를 올바르게
# f1 = open('test.txt', 'w')
# f1.write('Life is too short')
# f1.close()

# f2 = open('test.txt', 'r')
# print(f2.read())
# f2.close()
# print('=' * 50)

# 6. 사용자 입력을 파일에 저장하는 프로그램. 단, 기존꺼에 추가 되게
# user_input = input('저장할 말 입력 : ')
# f = open('test.txt', 'a')
# f.write(user_input)
# f.write('\n')
# f.close()

# 7. 파일에서 'java'라는 문자열을 'python'으로 바꾸기
"""
파일 내용 :

Life is too short
You need java
"""
f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()

# 다음엔 클래스