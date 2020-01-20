# 점프 투 파이썬 237page

# input('프롬프트에 띄울 말')
"""
a = input('숫자 입력 : ')
print(a)
"""
# int(): () 안에 있는 숫자를 정수형으로 변환
print(int(3.4))
print(int(3.6))
print('=' * 50)

# int(x, radix): radix 진수로 표현된 문자열 x 를 10진수로 변환하여 리턴한다.
print(int('11', 2))
print(int('63', 8))
print('=' * 50)

# isinstance(object, class): object가 class의 인스턴스이면 True 아니면 False 리턴

class Person: pass

a = Person()
print(isinstance(a, Person))

b = 3
print(isinstance(b, Person))
print('=' * 50)

# len(s): s의 길이 or 요소의 전체 개수
print(len('python.'))
print(len([1, 2, 3]))
print(len((1, 'a')))
print('=' * 50)

# list(s): 는 반복 가능한 자료형 s 을 입력 받아 리스트를 복사해 리턴한다.
print(list('python.'))
a = [1, 2, 3]
b = a
c = list(a)
print(a, id(a))
print(b, id(b))
print(c, id(c))
print('=' * 50)

# map(f, iterable): iterable의 각 요소가 함수 f를 통과한 결과를 묶어서 돌려준다.
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

def two_times2(number):
    return number * 2

print(list(map(two_times2, [1, 2, 3, 4])))
print('=' * 50)

# max(iterable): 입력된 iterable매개변수의 요소 중 최대값을 리턴
print(max([1, 2, 3, 6, 4]))
print(max('python'))
print('=' * 50)

# min(iterable): 입력된 iterable매개변수의 요소 중 최소값을 리턴
print(min([1, 2, 3, 6, 4]))
print(min('python'))
print('=' * 50)

# oct(): 정수형태 숫자를 8진수로 바꿔서 리턴
print(oct(3))
# print(oct(4.5))  # TypeError 발생
print('=' * 50)

# open(파일명, 모드): 모드 생략시 'r' 읽기 모드 기본으로 읽는다.
"""
w : 쓰기모드(파일 내용이 자동으로 지워진다.)
r : 읽기모드
a : 추가모드
b : 바이너리 모드로 파일 열기(w, r, a 와 함께 쓰인다.)
"""

# ord(): 문자의 아스키코드값을 리턴
print(ord('a'))
print(ord('0'))
# print(ord('aaa'))  # 이럼 TypeError에러
print('=' * 50)

# pow(x, y): x의 y 제곱
print(pow(4, 5))
print(pow(2, 3))
print('=' * 50)

# range([start,] stop [, step]): 입력 받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다.
print(list(range(5)))
print(list(range(1, 5)))
print(list(range(1, 5, 2)))
print(list(range(5, 0, -1)))
print('=' * 50)

# round(float [, ndigits]) 실수 입력 받아 반올림
print(round(3.424424332))
print(round(3.424424332, 2))
print(round(3.427424332, 2))
print('=' * 50)

# sorted(): iterable값을 입력받아 정렬 후 리스트로 리턴
print(sorted([1, 3, 2]))
print(sorted('python'))
print('=' * 50)

a = [1, 7, 3, 5, 4, 6]
b = sorted(a)
print(a)
print(b)
print('=' * 50)

# str(): 문자열 형태로 객체를 변환하여 리턴
a = 3
b = str(a) + '5'
print(b)
print('=' * 50)

# sum(iterable): 입력받은 리스트나 튜플의 모든 요소의 합을 돌려준다.
print(sum(range(6)))
print(sum([1, 2, 3, 4, 5]))
print(sum((1, 2, 3, 4, 5)))
# print(sum(['p', 'y', 't', 'h', 'o', 'n']))  # int만 됨
print('=' * 50)

# tuple(iterable): 반복 가능한 자료형을 입력 받아 튜플의 형태로 리턴한다.
print(tuple('abc'))
print(tuple([1, 2, 3]))
print(tuple((1, 2, 3)))

# type(): 입력값의 자료형을 리턴
print(type('abc'))
print(type([]))
print(type(()))
print(type(open('test.txt', 'w')))
print('=' * 50)

# zip(*iterable): 동일한 개수로 이루어진 자료형을 묶어주는 역할을 한다.
print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9, 10])))
print(list(zip('abc', 'def', 'ghij')))