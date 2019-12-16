# 점프 투 파이썬 

# 클래스

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(5))
print(cal2.add(7))
print('=' * 50)

# 가장 간단한 클래스의 예
class Cookie():
    pass

a = Cookie()
b = Cookie()

# 사칙연산 클래스 구상, 제작
# 두 숫자 입력 setdata, 나누기 div, 빼기 sub, 더하기 add, 곱하기 mul

# class FourCal:
#     pass

# a = FourCal()
# print(type(a))  # <class '__main__.FourCal'> : 클래스 a의 타입은 FourCal()이다.

class FourCal:
    def setdata(self, first, second):
    # 첫번째 매개변수 self에는 이 함수를 호출한 객체 a가 자동으로 전달 된다.
    # self 말고도 다른 이름으로 써도 같은 기능을 한다.
        self.first = first
        self.second = second
    
a = FourCal()
a.setdata(4, 2)
print(a.first, a.second)

# 클래스의 함수를 호출하는 다른 방법
FourCal.setdata(a, 5, 3)
print(a.first, a.second)
print('=' * 50)

