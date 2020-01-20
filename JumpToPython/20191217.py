# 점프 투 파이썬 207page ~

# ============================== 모듈 ==============================

import mod1

print(mod1.add(4, 3))
print(mod1.sub(4, 3))
print('=' * 50)

# 모듈 이름 없이 사용하는 방법 1
from mod1 import add
print(add(6, 4))
print('=' * 50)

from mod1 import *  # mod1에 있는 모든 함수를 사용하겠다는 의미
print(add(4, 3))
print(sub(4, 3))
print('=' * 50)

# 클래스나 변수 등을 포함한 모듈

import mod2

print(mod2.PI)
a = mod2.Math()
print(a.solv(2))
print(mod2.add(4, 2))
print('=' * 50)

# 다른 디렉토리에 있는 모듈 사용 방법.

# 1. sys.path.append(모듈을 설치한 디렉토리) 사용

# import sys
# print(sys.path)  # 여기에 포함된 경로에 있으면 바로 모듈을 불러서 사용 가능하다.
# sys.path.append('./Modules')
# print(sys.path)
# sys.path.pop()
# print(sys.path)


# 2.PYTHONPATH 환경변수 사용

# cmd에서
# set PYTHONPATH = D:\PythonExam\Modules 라고 쓴 후 사용
# set PYTHONPATH = D:\PythonExam\Modules

# ============================== 패키지 ==============================

"""
    패키지
    도트(.)를 활용해 파이썬의 모듈을 계층적으로 관리할 수 있게 해준다.

"""

# 패키지 내부 함수 실행 1
import game.sound.echo
game.sound.echo.echo_test()

# 패키지 내부 함수 실행 2
from game.sound import echo
echo.echo_test()

# 패키지 내부 함수 실행 3
from game.sound.echo import echo_test
echo_test()

# 불가능한 패키지 내부 함수 실행 방법
import game
game.sound.echo.echo_test()  # ??? 왜 됨???

# __init__.py 파일의 용도 .... 부터는 내일...

"""
    __init__ 파일은 해당 디렉토리가 패키지의 일부임을 알려주는 용도로 사용한다. 
    (python3.3부터는 없어도 인식하나 이전 버전과의 호환을 위해 남겨둔다.)

"""