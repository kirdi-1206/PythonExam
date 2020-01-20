# 점프 투 파이썬 146page 연습문제

# 1. 다음의 결과
a = 'Life is too short, you need python'
if 'wife' in a: print('wife')
elif 'python' in a and 'you' not in a: print('python')
elif 'shirt' not in a: print('shirt')
elif 'need' in a: print('need')
else: print('none')
print('=' * 50)

# 2. 1 ~ 1000 까지 3의 자연수 중 3의 배수의 합
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0: continue
    result += i
    i += i
print(result)
print('=' * 50)

# 3. while문을 사용하여 다음과 같이 *을 표시하는 프로그램 작성
"""
*
**
***
****
*****
"""
i = 0
while True:
    i += 1
    if i > 5: break
    print('*' * i)
print('=' * 50)

# 4. for문을 사용하여 1~ 100까지 출력
for i in range(1, 101):
    print(i)
print('=' * 50)

# 5. A학습에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다 
#    for문을 사용하여 이 학급의 평균 점수를 계산해보자
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)
print('=' * 50)

# 6. 리스트 중 홀수에만 2를 곱하여 저장하는 코드가 있다.
number = [1, 2, 3, 4, 5]
result = []
for n in number:
    if n % 2 == 1:
        result.append(n * 2)
# 위 코드를 리스트 내포(list comprehension)를 사용하여 표현해보자
result = [n * 2 for n in number if n % 2 == 1]
print(result)
print('=' * 50)
print('=' * 50)

# ============================== 프로그램 입출력 ==============================

# 함수
def add(a, b):
    return a + b
a = 3
b = 4
c = add(a, b)
print(c)
print('=' * 50)

# 입력값이 없는 함수
def say():
    return 'hi'
print(say())
print('=' * 50)

# 결과값이 없는 함수
def add_print(a, b):
    print('%d와 %d의 합은 %d 입니다.' %(a, b, a + b))
add_print(4, 6)
print(add_print(4, 6))
print('=' * 50)

# 입력도 결과값도 없는 함수
def say2():
    print('hi')
say2()

# 함수 매개변수 지정
result = add(a = 3, b = 5)
result = add(b = 5, a = 3)  # 매개변수를 지정하면 순서에 상관 없이 사용 할 수 있다.

# 입력값에 개수가 정해지지 않은 함수
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result
result = add_many(1, 2, 3, 4, 5)
print(result)
print('=' * 50)

def add_mul(choice, *args):
    result = 0
    if choice == 'add':
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    return result
print(add_mul('add', 1, 2, 3, 4, 5))
print(add_mul('mul', 1, 2, 3, 4, 5)) 
print(add_mul('aaa', 1, 2, 3, 4, 5))
print('=' * 50)

# 키워드 파라미터
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(name = 'foo', age = 3)
# print_kwargs(name = 'foo', age = 3, 'bb')  # 딕셔너리만 매개변수로 가능
print('=' * 50)

# 결과값은 하나뿐 이다.
def add_add_mul(a, b):
    return a + b, a * b
print(add_add_mul(3, 5))  # 튜플 형태로 반환된다
print('=' * 50)

# return의 또 다른 쓰임새
def say_nick(nick):
    if nick == '바보':
        return  # 여기서 바로 빠져나간다. 델파이에 Exit 같은 것
    print('나의 별명은 %s 입니다.' %nick)
say_nick('바보')
say_nick('보비')
print('=' * 50)

# 매개변수 default 값 설정
def say_myself(name, old, man = True):
    print('나의 이름은 ' + name + ' 입니다.')
    print('나의 나이는 ' + str(old) + '살 입니다.')
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')
say_myself('김개똥', 20, True)
say_myself('김개똥', 20)
say_myself('김말숙', 20, False)
print('=' * 50)
# default 값 설정은 맨 뒤에만 된다.
def say_myself2(name, old = 22, man = True):  # 이렇게는 가능함
    print('나의 이름은 ' + name + ' 입니다.')
    print('나의 나이는 ' + str(old) + '살 입니다.')
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')
say_myself2('김개똥')
print('=' * 50)

# 함수 안에서 선언한 변수의 효력
a = 1
def vartest(a):
    a += 1
vartest(a)
print(a)

# 함수 안에서 함수 밖에 변수를 변경하는 방법
# 방법 1
a = 1
def vartest2(a):
    a = a + 1
    return a
a = vartest2(a)
print(a)

# 방법 2
b = 2
def vartest3():
    # global b += 1  # 한줄에 쓰는건 안됨
    global b         # 외부에 종속적인 함수를 만드는게 좋은게 아니므로 자제할것 방법1을 권함
    b += 1
vartest3()
print(b)
print('=' * 50)

# 람다식

# 사용법 : lambda 매개변수1, 매개변수2, ... : 매개변수를 사용한 표현식
add2 = lambda a, b : a + b
result = add2(3, 4)
print(result)
print('=' * 50)
print('=' * 50)

# ============================== 사용자 입출력 ==============================

# 사용자 입력

# input 사용 *실행시 주석 풀어서 사용할 것
# a = input()
# print(a)
# print('=' * 50)
# a = input('하고싶은말 : ')  # 이런식으로도 사용 가능함.
# print(a)
# print('=' * 50)

# print문으로 할 수 있는 일
print("Life" "is" "too" "short")
print("Life" + "is" + "too" + "short")
print("Life", "is", "too", "short")
for i in range(10):
    print(i, end = ' ')  # 끝 문자를 엔터가 아닌 다른 문자로
print()                  # 이렇게 엔터 하나 넣어줌

