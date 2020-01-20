# 점프 투 파이썬 독학 1

"""
여러 줄 짜리 주석이다.
큰 따옴표를 3개 씩 쓰면 된다.
"""
'''
작은 따옴표 3개도 된다.
그렇지?
'''
print('Hello World!')

# 파이썬의 자료형

# 숫자형

a = 0o34  # 8진수
b = 0x2a  # 16진수
print(a, b)

# 실수의 소수점 표현 방식
a = 4.25e10
b = 4.25e-1
print(a, b)

# 사칙연산은 동일 +, -, *, /

print(3 ** 4)  # 3의 4제곱 '**'
print(7 % 3)   # 7을 3으로 나눈 나머지
print('7 / 4 : ' + str(7 / 4) + ', 7 // 4 : ' + str(7 // 4)) # 나눈 몫을 반환하는 '//'

# 문자열
a = "Hello world"
print(a)

a = 'Python is good'
print(a)

a = """Hello world"""
print(a)

a = '''Python is good'''
print(a)

a = 'I said "Python is good"' # 문자열에 큰 따옴표(")를 포함하고 싶을 때
print(a)

a = "I'm programmer" # 문자열에 따옴표(')를 포함하고 싶을 때
print(a)

a = '\', \\, \"' # 문자열에 큰 따옴표, 따옴표, 역슬래시를 포함 시킬 때
print(a)

# 여러줄 출력
multiline = '이건 파이썬에서 \n두 줄을 사용하기 위한 나의 예시'
print(multiline)

multiline = '''
이건 파이썬에서
여러줄을 사용하기 위한 나의 예시
'''
print(multiline)

# 문자열 연산
print('익히' + ' 아는' + ' 이것')
print('이건 처음 볼 껄?' * 2)
print('=' * 50)

# 문자열 길이
stringdata = '안녕'
a = len(stringdata)  # 2
print(str(a))
stringdata = 'abc'
a = len(stringdata)  # 3
print(str(a))
print('=' * 50)

# 문자열 인덱싱 첫 글자가 0부터 시작한다.
stringdata = 'Life is short, You need Python'
print(stringdata[3])
stringdata = '삶은 짧아, 너는 파이썬이 필요할꺼야'
print(stringdata[1])
print('=' * 50)

# 문자열 인덱싱 2
a = 'Life is short, You need Python'
print(a[-1])
print(a[-10])
print('=' * 50)

# 문자열 슬라이싱
a = 'Life is short, You need Python'
b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0:4])
print('=' * 50)

# 문자열 슬라이싱 2
a = 'Life is short, You need Python'
print(a[15:])

# 문자열 슬라이싱 3
a = '20191205224933'
date = a[:8]
time = a[8:12]
print(date + ' ' + time)
print('=' * 50)

# 문자열 수정
a = 'Pithon'
print(a[:1])
print(a[2:])
print(a[:1] + 'y' + a[2:])
print('=' * 50)

# 문자열 포매팅
number = 10
day = 'three'
print('I ate %d apples. so I was sick for %s days.' %(number, day))

"""
문자열 포매팅코드
%s : 문자열
%c : 문자 1개
%d : 정수
%f : 부동소수
%o : 8진수
%x : 16진수
%% : Literal % (문자 '%' 자체)
"""

print('1 + 2.5 = %s' %3.5)  # %s를 사용하면 실수든 정수든 사용할 수 있다.
print('1 + 2 = %s' %3)

# print('Loding... %d%.' %98)  # 실행시 ValueError: incomplete format 에러가 발생한다
print('Loding... %d%%' %98)  # 이렇게 해야 위의 에러가 안난다.
print('=' * 50)

# 정렬과 공백
print('%10s' % 'hi') # 좌측 10칸 공백
# print('%10s hi' %) # 이건 에러

print('%-10sjane' % 'hi')
print('=' * 50)

# 소수점 표현
print('%0.4f' % 3.141592)
print('[%10.4f' % 3.141592 + ']')
print('[%-10.4f' % 3.141592 + ']')
print('=' * 50)

# format 함수 사용
print('I eat {0} apples'.format(3))
num = 5
print('I eat {0} apples'.format(num))
num = 3
day = 'three'
print('I ate {0} apples. so I was sick for {1} days.'.format(num, day))
print('=' * 50)

# format 함수 사용 2
print('I ate {num} apples. so I was sick for {day} days.'.format(num = 5, day = 'four'))
num = 3
print('I ate {0} apples. so I was sick for {day} days.'.format(num, day='four'))

# format 함수 사용 3 : 정렬
print('[{0:<10}'.format('hi') + ']') # 왼쪽
print('[{0:>20}'.format('hi') + ']') # 오른쪽

# ~ 63page