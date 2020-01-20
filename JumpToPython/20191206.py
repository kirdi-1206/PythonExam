# 점프 투 파이썬 64p ~

# 정렬
print('[{0:^10}'.format('hi') + ']')
print('=' * 50)

# 공백 채우기
print('{0:=^10}'.format('hi'))
print('{0:=<10}'.format('hi'))
print('{0:=^10}'.format('hi'))
print('=' * 50)

# 소수점 표현
y = 3.42134234
print('{0:0.4f}'.format(y))  # 소수 4자리 까지만 보여준다.
print('{0:10.4f}'.format(y))  # 앞에 공백 포함 10자리 그리고 소수 4자리 까지만 보여준다.
print('=' * 50)

# {또는} 문자표현
print('{{and}}'.format())
print('=' * 50)

# f 문자열 포매팅, python 3.6 이상만 된다.
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.\n 내년에 {age + 1}살이 됩니다.')
print('=' * 50)

# f 문자열 포매팅 - 정렬
print('[' + f'{"hi":<10}' + ']')
print('[' + f'{"hi":^10}' + ']')
print('[' + f'{"hi":>10}' + ']')
print('=' * 50)

# f 문자열 포매팅 - 공백채우기
print('[' + f'{"hi":=<10}' + ']')
print('[' + f'{"hi":=^10}' + ']')
print('[' + f'{"hi":=>10}' + ']')
print('=' * 50)

# f 문자열 포매팅 - 소수점 표현
y = 3.42134234
print(f'{y:0.4f}')
print('[' + f'{y:10.4f}' + ']')
print('=' * 50)

# f 문자열 포매팅 {} 사용
print(f'{{}}')
print('=' * 50)

# 나혼자 코딩
print('{0:!^12}'.format('python'))
print(f'{"python":!^12}')
print('=' * 50)

# ========================= 문자열 관련 함수 =========================

# count
a = 'hobby'
print(a.count('b')) # 'b'의 개수
print('=' * 50)

# find
a = 'Python is best choice, I like programming.'
print(a.find('i'))  # 문자열은 0부터 시작. 제일 처음 나온 위치 반환
print(a.find('I'))  # 대소문자 구별
print(a.find('z'))  # 없으면 -1
print('=' * 50)

# index
# print(a.index('z'))  # index 함수는 없으면 ValueError: substring not found 에러

# join - 문자열 삽입
print(','.join('abcd'))  # 각각의 문자 뒤에 ',' 삽입
print(','.join(['ab', 'cd']))  # 각각의 원소 뒤에 ',' 삽입
print('=' * 50)

# upper - 소문자 -> 대문자
print('Hi'.upper())

# lower - 대문자 -> 소문자
print('Hi'.lower())
print('=' * 50)

# 공백 지우기
print('[' + ' \n  hi'.lstrip() + ']') # lstrip - 왼쪽
print('[' + 'hi \n  '.rstrip() + ']') # rstrip - 오른쪽
print('[' + ' \n  hi \n  '.strip() + ']') # strip - 양쪽
print('=' * 50)

# replace - 문자열 바꾸기
a = 'Life is too short'
a.replace('Life', 'Your legs')
print(a)  # a를 바꾸는게 아니라 출력만 그렇게 나온다. a를 바꾸고 싶으면 넣어줘야 함
print(a.replace('Life', 'Your legs'))
print('=' * 50)

# split - 문자열 나누기
a = 'Life is too short'
print(a.split())  # 공백을 기준으로 문자열을 나눈다.
b = 'a:b:c:d'
print(b.split(':')) # ':'을 기준으로 문자열을 나눈다
print('=' * 50)

# ============================== 리스트 자료형 ==================================

# 아래 형태 모두 가능
a = []
b = [1, 2, 3]
c = ['life', 'is', 'too', 'short', '!']
d = [1, 2, 'life', 'is']
e = [1, 2, ['life', 'is']]

print(b)
print(b[0] + b[2])
# print(b[0] + c[0]) # TypeError 발생
print(e[-1])
print(e[-1][0])
print('=' * 50)

# 리스트 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])
print(a[:2])
print(a[1:])
print('=' * 50)

# 리스트 더하기
print(a + b)
print((a + b)[3:])

# 리스트 반복
print(a * 3)

# len - 리스트의 길이
print(len(a))

# 리스트 요소 수정
a = [1, 2, 3, 4, 5]
a[2] = 7
print(a)
print('=' * 50)

# del - 리스트 삭제
# del 객체, 형태로 파이썬에서 사용하는 모든 자료형을 삭제할 수 있다.
del a[2]
print(a)
print('=' * 50)

# append - 리스트 추가
a = [1, 2, 3]
a.append(4)
print(a)
# a.append(5, 6) # 이건 에러
a.append([5, 6])
print(a)

# sort - 리스트 정렬
a = [1, 4, 3, 2, 7, 5, 6]
b = ['bdef', 'abc', 'ged']
c = ['f', 'b', 'a', 'c', 'e', 'd']
a.sort()
b.sort()
c.sort()
print(a)
print(b)
print(c)
print('=' * 50)

#  ~ 80 page