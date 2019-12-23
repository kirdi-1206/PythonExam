# 점프 투 파이썬

# ============================== 파이썬 외장 함수 ==============================

# ==================== sys 모듈 ====================

# 명령 행에서 인수 전달 - sys.argv
import sys
print(sys.argv)
print('=' * 50)

"""
CMD 창을 열어서 아래와 같이 실행하면 알 수 있다.
D:\PythonExam>python 20191223.py you need pyhon
['20191223.py', 'you', 'need', 'pyhon']
"""

"""
CMD 창에서 
>>>import sys
>>>sys.exit()
라고 쓰면 파이썬 스크립트가 강제 종료 된다. 
"""

print(sys.path)  # 참고하고 있는 경로가 모두 표시된다.
# sys.path.append 함수로 경로를 추가 할 수 있다.
print('=' * 50)


# ==================== pickle ====================
# 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈

import pickle
# 저장하기 dump
f = open('test.txt', 'wb')  # 'b' 를 써줘야 오류가 안난다.
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

# 불러오기 load
f = open('test.txt', 'rb')  # 'b' 를 써줘야 오류가 안난다.
data = pickle.load(f)
print(data)
f.close()
print('=' * 50)

# ==================== os ====================
# 환경변수나 디렉토리, 파일 등 OS 자원을 에어 할 수 있게 해준다.
import os

# 시스템의 환경변수 os.environ
print(os.environ)
print('=' * 50)
print(os.environ['PATH'])  # 환경변수중 PATH 만
print('=' * 50)

# 디렉터리 위치 변경 - CMD에서 된다.
os.system('dir')  # 바뀐 위치를 확인 할 수 있다.
print('=' * 50)
os.chdir('C:\WINDOWS')
os.system('dir')  # 바뀐 위치를 확인 할 수 있다.
print('=' * 50)
os.getcwd()
print('=' * 50)

# 시스템 명령어 호출
os.chdir('D:\PYTHONEXAM')
os.system('dir')
print('=' * 50)

# 실행한 시스템 명령어의 결괏값 돌려받기 - os.popen
f = os.popen('dir')
print(f.read())
print('=' * 50)

# 기타 os 관련함수
# os.mkdir(디렉토리) : 디렉토리 생성
# os.rmdir(디렉토리) : 디렉토리 삭제
# os.unlink(파일명)  : 파일 삭제
# os.rename(src, dst): src파일의 이름을  dst로 수정

# ==================== shutil ====================
# 파일을 복사해주는 파이썬 모듈
import shutil
shutil.copy('test.txt', 'dst.txt')  # 파일 생성 및 내용 복사

# ==================== glob ====================
# 특정 디렉터리의 파일 이름을 모두 알아야 할 때 사용
import glob
# 디렉토리에 있는 파일을 리스트로 만든다.
print(glob.glob(os.getcwd() + '/*'))
print('=' * 50)

# ==================== tempfile ====================
# 파일을 임시로 만들어 사용할 때 사용한다.
import tempfile
filename = tempfile.mktemp()
print(filename)  # 경로에 가보면 바로 삭제된걸 알 수 있다.
print('=' * 50)

f = tempfile.TemporaryFile() 
# 임시 저장 공간으로 사용할 파일 객체를 돌려준다.
# 이 파일은 자동적으로 바이너리 쓰기 모드를 갖는다.
f.close()  
# .close() 함수를 만나면 생성한 파일 자동 삭제된다.

# ==================== time ====================
import time
# time.time() UTC 를 사용하여 현재 시간을 실수로 리턴
print(time.time())
print('=' * 50)
print(time.localtime())
print(time.localtime(time.time()))
print('=' * 50)
print(time.asctime())
print(time.asctime(time.localtime(time.time())))
print('=' * 50)
print(time.ctime())
print('=' * 50)
print(time.strftime('%x', time.localtime()))

# time.sleep : 시간 잠시 멈춤
for i in range(10):
    print(i)
    # time.sleep(1)  # 1이면 1초씩 멈춤
print('=' * 50)

# ==================== calendar ====================
import calendar

print(calendar.calendar(2019))
print('=' * 50)
calendar.prcal(2015)
print('=' * 50)

print(calendar.weekday(2019, 12, 23))  # 0: 월, 1: 화, ... , 6:일
print(calendar.monthrange(2019, 12))
# (6, 31) 가 출력된다 첫째날은 6: 일요일이고 31일까지 있음을 알려준다.
print('=' * 50)

# ==================== random ====================
import random

print(random.random())  # 0.0 ~ 1.0 사이의 실수
print(random.randint(1, 10)) # 1 ~ 10 사이의 정수
print('=' * 50)

def random_pop(data):
    # 리스트에서 무작위로 꺼낸 다음 그 값을 올려주고 삭제 시킨다.
    number = random.randint(0, len(data) - 1)
    return data.pop(number)

def random_pop2(data):
    # 리스트에서 무작위로 꺼낸 다음 그 값을 올려주고 삭제 시킨다.
    number = random.choice(data)
    data.remove(number)
    return number

data = [1, 2, 3, 4, 5]
while data: print(random_pop(data))
print('=' * 50)
data = [1, 2, 3, 4, 5]
while data: print(random_pop2(data))

# shuffle(data): 리스트의 항목을 무작위로 섞는다.
data = [1, 2, 3, 4, 5]
random.shuffle(data)
print(data)

# ==================== webbrowser ====================
# 자신의 시스템에서 사용하는 기본 웹브라우저를 자동으로 실행하는 모듈
import webbrowser
# webbrowser.open('https://github.com/flagman1211/PythonExam')
# webbrowser.open_new('https://google.com')  


# ==================== threading: 스레드 ====================
import time

def long_task():
    for i in range(5):
        time.sleep(1)
        print('working:%s\n' %i)
    
# print('Start')
# for i in range(5):
#     long_task()
# print('End')
# 위 함수는 25초 정고 걸리는데 스레드를 사용해 5초의 시간이 걸리는 long_task 함수를 동시에 실행한다.

import threading

print('Start')
threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)
for t in threads:
    t.start() # 스레드를 시작한다..
for t in threads:
    t.join()  # join으로 스레드가 종료될 때 까지 기다린다.
print('End')