# Chapter 01 숫자

# 1.2 부동소수점

# 1.2.1 부동소수점 비교
# 부동소수점은 이진수 분수로 표현되므로 함부로 비교 / 연산하면 안된다.

print(0.2 * 3 == 0.6)
print(1.2 - 0.2 == 1.0)
print(1.2 - 0.1 == 1.1)
print(0.1 * 0.1 == 0.01)
print('=' * 50)

# 동등성 테스트는 사전 정의된 정밀도 범위 안에서 이루어져야한다.

def CompareFloat(x, y, places = 7):
    return round(abs(x - y), places) == 0

print(CompareFloat(0.2 * 3, 0.6))
print(CompareFloat(1.2 - 0.2, 1.0))
print(CompareFloat(1.2 - 0.1, 1.1))
print(CompareFloat(0.1 * 0.1, 0.01))
print('=' * 50)

# 1.2.2 정수와 부동소수점 메서드
# /  : 항상 부동소수점으로 반환
# // : 정수로 반환
# divmod(x, y) : x를 y로 나눈 몫과 나머지
# round(x, n) : n 이 음수이면 x를 n자리에서 반올림한 값. n이 양수이면 x를 소수점 이하 n자리로 반올림한 값을 반환한다.
# as_integer_ratio() : 부동소수점수를 분수로 표현

print(6 / 3)
print(7 // 3)
print(divmod(7, 3))
print(round(100.96, -10))
print(round(100.96, 2))
print(2.75.as_integer_ratio())