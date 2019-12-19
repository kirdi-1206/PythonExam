# 점프 투 파이썬 219page

# __init__.py 파일의 용도

# from game.sound import *
# echo.echo_test()  # NameError: name 'echo' is not defined 에러 발생(__init__.py 파일에 __all__ 변수를 설정하지 않았을 경우)

# 특정 디렉토리의 모듈을 *을 사용하여 import 할 때는 
# 해당 디렉토리의 __init__.py 파일에 __all__ 변수를 설정하고 import할 수 있는 모듈을 정의해줘야 한다.
"""
    game/sound/__init__.py 내용 추가
    __all__ = ['echo']
"""
from game.sound import *
echo.echo_test() # 이거 에러 아님. 왜 뜨는지 모르겠음....!!!!
print('=' * 50)

# ==================== reavrive 패키지 ====================

# 만약 graphic 디렉토리의 render.py 모듈에서 sound 디렉토리의 echo.py 모듈을 사용하려는 경우
# render.py 모듈을 다음과 같이 수정한다
"""
from game.sound.echo import echo_test
def render_test():
    print('render')
    echo_test
"""
from game.graphic import render
render.render_test()
print('=' * 50)

# from game.sound.echo import echo_test 대신에
# from ..sound.echo import echo_test라고 쓰는 것으로도 가능하다.
# sound 앞에 '..'은 상위 디렉토리를 의미한다.


# ============================== 예외 처리 ==============================

# 대표적 오류 3가지
# f = open('없는파일', 'r')  # FileNotFoundError: [Errno 2] No such file or directory: '없는파일'
# a = 4 / 0                 # ZeroDivisionError: division by zero
# a = [1, 2, 3]
# a[4]                      # IndexError: list index out of range

# ========== 예외 처리 기법 ==========

# try, except 1.
try:
    f = open('없는파일', 'r')
except:
    print('에러 발생이네')
print('=' * 50)

# try, except 2.
try:
    a = 4 / 0 
    f = open('없는파일', 'r')
except ZeroDivisionError:
# f = open('없는파일', 'r') 에서 FileNotFoundError가 에러가 발생하더라도 
# a = 4 / 0 에러가 먼저 걸러짐으로 에러가 발생하지 않음
    print('0으로 나눴네')
print('=' * 50)

# try, except 3.
try:
    f = open('없는파일', 'r')
except FileNotFoundError as e:  # 에러메시지 e를 받음 (다른 이름으로 해도 상관 없음)
    print(e)
print('=' * 50)

# 여러개의 예외 처리.
try:
    a = 4 / 0 
    f = open('없는파일', 'r')
except ZeroDivisionError as e:
    print('0으로 나눴네')
    print(e)
except FileNotFoundError as e:
    print('없는 파일이네')  # ZeroDivisionError 가 먼저 발생함으로 위쪽으로 빠진다.
    print(e)
print('=' * 50)

try:
    a = 4 / 0 
    f = open('없는파일', 'r')
except (ZeroDivisionError, FileNotFoundError) as e:
    print('0으로 나눴거나 파일이 없네')
    print('정확한 에러는', e)
print('=' * 50)

# ==================== 오류 회피 ====================
try:
    f = open('없는파일', 'r')
except:
    pass
print('=' * 50)

# ==================== 오류 강제 발생 ====================

# 에러를 강제로 발생시키고 싶은 경우 raise 명령어를 사용한다.

class Bird:
    def fly(self):
        raise NotImplementedError  # 상속받은 클래스로 하여금 fly 함수를 반드시 구현하게 한다.

class Eagle(Bird):
    pass
eagle = Eagle()
# eagle.fly()  # NotImplementedError 에러 발생

class Hork(Bird):
    def fly(self):
        print('very fast')
hork = Hork()
hork.fly()
print('=' * 50)

# ==================== 예외 만들기 ====================

# 특수한 경우에만 예외처리를 하기 위해 예외를 만들어 사용하기도 한다.
# 예외는 파이썬 내장 클래스인 Exception 클래스를 상속하여 만들 수 있다.
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

say_nick('천사')
# say_nick('바보')  # __main__.MyError 가 발생했다고 메시지가 출력된다.
print('=' * 50)

try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print('허용할 수 없는 별명입니다.')
    print(e)  # 아무것도 출력되지 않음을 볼 수 있다.
print('=' * 50)

# 에러메시지 출력을 위한 예외처리 클래스
class MyError2(Exception):
    def __str__(self):
        return '날 바보라고 부르는 것은 참을 수 없어!!'

def say_nick2(nick):
    if nick == '바보':
        raise MyError2()
    print(nick)

try:
    say_nick2('바보')
except MyError2 as e:
    print(e)
print('=' * 50)

# ============================== 파이썬 내장 함수 ==============================

# abs(): 절대값
print(abs(-3)) 
print('=' * 50)

# all(): 순서가 있는 자료형(list, tuple, string, dictionaly)의 경우 모두 참이면 True 하나라도 거짓이면 False를 리턴
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))
print('=' * 50)

# any(): 순서가 있는 자료형(list, tuple, string, dictionaly)의 경우 하나라도 참이면 True 모두 거짓이면 False를 리턴
print(any([1, 2, 0]))
print(any([0, '']))
print('=' * 50)

# chr(): 아스키 코드 값을 입력 받아 문자를 출력
print(chr(97))
print('=' * 50)

# dir(): 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.
print(dir([1, 2, 3]))
print('=' * 50)
print(dir({1:'a'}))
print('=' * 50)

# divmod(a, b): 숫자 2개를 입력 받아 a를 b로 나눈  몫과 나머지를 튜플 형태로 돌려준다.
print(divmod(7, 3))
print('=' * 50)

# enumerate(): 순서가 있는 자료형(list, tuple, string, dictionaly)을 입력 받아 인덱스 값을 포함하는 enumerate 객체로 돌려준다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
print('=' * 50)

# eval(): 실행 가능한 문자열을 실행해 결과를 돌려준다. ('1 + 2' or 'hi' + 'a')
print(eval('1+2'))
print(eval("'hi' + 'a'"))
# print(eval("hi + a"))  # 이건 NameError: name 'hi' is not defined 에러 난다.
print(eval('divmod(4, 3)'))  # 보통 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용한다.
print('=' * 50)

# filter(함수명, 반복 가능한 자료형(list, tuple, string, dictionaly)): 매개변수로 넘어온 함수의 반환 값이 참인 것만 결과를 돌려준다.
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1, -3, 2, 0, -5, 6]))
print('=' * 50)

# 위 함수를 아래처럼 구현할 수 있다.
def positive2(x):
    return x > 0

print(list(filter(positive2, [1, -3, 2, 0, -5, 6])))
print('=' * 50)

# hex(): 정수를 입력 받아 16진수로
print(hex(246))
print('=' * 50)

# id(): 객체 고유 주소 값을 리턴
a = 3
print(id(a))  # 1.
print(id(3))  # 2.
b = a
print(id(b))  # 3.   1, 2, 3 모두 같은 주소를 가르킨다.
print(id(4)) 
print('=' * 50)

# 236 page 까지 함...