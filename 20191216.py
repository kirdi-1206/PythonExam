# 점프 투 파이썬 192 page~

class FourCal:
    def setdata(self, first, second):
        self.first = first    # 매개변수로 온 first를 클래스 내부 변수 first에 넣는다.
        self.second = second  # 위와 마찬가지
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
        
a = FourCal()
b = FourCal()
# print(a.first)  # 여기서 실행하면 AttributeError: 'FourCal' object has no attribute 'first' 에러 발생
a.setdata(4, 2)
print(a.first, a.second, id(a.first))
b.setdata(3, 2)
print(b.first, b.second, id(b.first))
print('=' * 50)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
print('=' * 50)

# ==================== 생성자 ====================
# 메소드 이름이 __init__ 이면 생성자이다.
class FourCal2:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first    # 매개변수로 온 first를 클래스 내부 변수 first에 넣는다.
        self.second = second  # 위와 마찬가지
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

# a = FourCal2() 생성자의 매개변수에 값을 넣지 않으면 TypeError: __init__() missing 2 required positional arguments 에러
a = FourCal2(4, 2)

# class FourCal3 : FourCal2  # 이게 뭘까...? 왜 컴파일 에러가 안날까...?

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print('=' * 50)

# ==================== 클래스 상속 ====================

class MoreFourCal(FourCal2):
    # pass
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 3)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print('=' * 50)

print(a.pow())

# ==================== 오버라이드 ====================
class SafeForCal(FourCal2):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
            # super.div()

a = SafeForCal(4, 0)
print(a.div())

# ==================== 클래스 변수 ====================
class Family:
    lastname = '김'
print(Family.lastname)
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)
Family.lastname = '박'
print(a.lastname)
print(b.lastname)
print('Family : %s, a : %s, b : %s' %(id(Family.lastname), id(a.lastname), id(b.lastname)))  # 3개의 주소가 모두 같다
a.lastname = '서'
print(Family.lastname)
print(a.lastname)
print(b.lastname)
print('Family : %s, a : %s, b : %s' %(id(Family.lastname), id(a.lastname), id(b.lastname)))  # Family와 b만 같다.
b.lastname = '유'
print(Family.lastname)
print(a.lastname)
print(b.lastname)
print('Family : %s, a : %s, b : %s' %(id(Family.lastname), id(a.lastname), id(b.lastname)))  # 셋다 모두 다르다.
Family.lastname = '홍'
print(Family.lastname)
print(a.lastname)
print(b.lastname)
print('Family : %s, a : %s, b : %s' %(id(Family.lastname), id(a.lastname), id(b.lastname)))  # 셋다 모두 다르다.


