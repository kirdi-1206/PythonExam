# Chapter 01 숫자

# 1.1 정수
'''
int / 불변형 / 적어도 4byte
'''

# .bit_length() : 정수의 바이트 수 반환
# *.파이썬 3.1 이상
print((999).bit_length())  # 10 : 10바이트

# int(문자열, 밑) 문자열 정수 변환 및 다른 진법의 문자열을 정수로 변환
s = '11'
d = int(s)     # 10진수인 s를 10진수 정수로
print(d)
b = int(s, 2)  # 2진수인 s를 10진수 정수로
print(b)
s = '12'
# b = int(s, 2)  # 이렇게 실행하면 2진수 '12'는 존재할 수 없으므로 ValueError가 발생한다.
print(b)