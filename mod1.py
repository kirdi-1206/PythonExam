# 20191217.py 에서 사용하는 모듈
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# print(add(1, 4))  
# print(sub(4, 2))  
# 위 처럼 만 사용하면 다른 모듈에서 import 할 때 print의 결과가 출력된다.
# 이를 방지하려면 아래와 같이 바꾼다.

if __name__ == '__main__':  # 직접 mod1.py를 실행 했을때만 참이 되어 실행된다.
    print(add(1, 4))  
    print(sub(4, 2))

# __name__ 란?
# 파이썬 내부에서 사용하는 특수한 변수명이다.
# 직접 현재 파일을 실행할 경우에는 '__main__' 이라는 값이 들어가지만
# 다른 모듈에서 import 할 경우에는 확장자를 제외한 모듈의 이름 값이 저장 된다.