# 점프 투 파이썬 107page ~

# 변수
a = 1
b = 'python'
c = [1, 2, 3]
print(id(a), id(b), id(c)) # id(변수명) 변수의 메모리 주소
print('=' * 50)

# 리스트 복사
a = [1, 2, 3]
b = a
print(id(a), id(b)) # a와 b의 주소가 같다 => 주소가 복사된것 a를 고치면 b에도 반영됨
print(a is b)       # a is b : a와 b가 동일한가? True : False
a.append(4)
print(a, b)         # 둘 다 똑같이 4가 생겼다
print('=' * 50)

# [:]를 사용한 복사
a = [1, 2, 3]
b = a[:]
print(id(a), id(b))
print(a is b)
a.append(4)
print(a, b)
print('=' * 50)

# copy 모듈을 사용한 복사 
from copy import copy
a = [1, 2, 3]
b = copy(a)          # b = a[:] 와 동일
print(id(a), id(b))
print(a is b)
a.append(4)
print(a, b)
print('=' * 50)

# ==================== 그냥 넘어갈 수 없는 복사쓰 ====================

# 단순 객체 복제
a = [1, 2, 3, 4]
b = a
print('a =', a, ', b =', b, ', a = b ? :', a is b)
a[3] = 7
print('a =', a, ', b =', b, ', a = b ? :', a is b)
# 위는 a, b 모두 수정됨 mutable객체만 그럼 immutable객체는 안그럼
a = 10
b = a
print('a =', a, ', b =', b, ', a = b ? :', a is b)
b = 'abc'
print('a =', a, ', b =', b, ', a = b ? :', a is b)
print('=' * 50)
"""
정리!!
immutable 객체 : 숫자형, 문자열, 튜플(1, 2, ...)      -> Call by Value
mutable 객체   : 리스트, 딕셔너리 {1:'a', 2:'b', ...} -> Call by Reference
"""
import copy
# 얕은 복사
a = [1, [1, 2, 3]]
b = copy.copy(a)
print('a =', a, ', b =', b, ', a = b ? :', a is b)
b[0] = 100
print('a =', a, ', b =', b, ', a = b ? :', a is b) # 이건 b만 바뀜
b[1].append(4)
print('a =', a, ', b =', b, ', a = b ? :', a is b) # 이건 둘 다 바뀜
# 내부 리스트가 참조하고 있는 주소가 같아서 그런거
print('a[1] = b[1] ?', a[1] is b[1])               # 주소 같은거 확인 가능
print('=' * 50)

# 깊은 복사
a = [1, [1, 2, 3]]
b = copy.deepcopy(a)
print('a =', a, ', b =', b, ', a = b ? :', a is b)
b[0] = 100
print('a =', a, ', b =', b, ', a = b ? :', a is b) # 이렇게 해도
b[1].append(4)
print('a =', a, ', b =', b, ', a = b ? :', a is b) # 이렇게 해도 안바뀜
print('a[1] = b[1] ?', a[1] is b[1])               # 주소 달라진거 확인 가능
print('=' * 50)

# 다시 변수 얘기.........

# 변수를 만드는 방법

# 튜플 방식
a, b = ('python', 5)  # 아래와 같다.
print(a, b)
(a, b) = 'python', 5  # 위와 같다
print(a, b)
print('=' * 50)

# 리스트 방식
[a, b] = ['python', 5]
print(a, b)
a, b = ['python', 5]
print(a, b)
[a, b] = 'python', 5
print(a, b)
print('=' * 50)

# 여러변수에 같은 값 대입
a = b = 'python'
print(a, b)
print('=' * 50)

# 응용
a = 5
b = 'a'
a, b = b, a
print(a, b)  # 서로 뒤바뀜
print('=' * 50)

# 연습문제 112page

# 1
grade = {'kor' : 80, 'eng' : 75, 'math' : 55}
print('길동이의 평균성적 : ', (grade.get('kor') + grade.get('eng') +  grade.get('math')) / len(grade))   # 이건 소수점까지
print('길동이의 평균성적 : ', (grade.get('kor') + grade.get('eng') +  grade.get('math')) // len(grade))  # 이건 소수점이 없고

# 2
if 13 % 2 == 0 :
    print('13 is even')
else :
    print('13 is odd')

# 3
pin = '881120-1068234'
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd, num)

# 4
if pin[7] == '1' :
    print('남 자')
else :
    print('여 자')

# 5
a = 'a=b=c=d'
b = a.replace('=', '#')
print(b)

# 6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 7
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)

# 8
a = (1, 2, 3)
a = a + (4,)
print(a)

# 9
a = dict()
print(a)
a['name'] = 'python'
print(a)
a[('a',)] = 'python'
print(a)
# a[[1]] = 'python'  # unhashable type: 'list' Key에 변할 수 있는 list형은 못들어간다.
# print(a)
a[250] = 'python'
print(a)

# 10
a = {'A' : 90, 'B' : 80, 'C' : 70}
result = a.pop('B')
print(a)
print(result)

# 11
a = [1, 1, 1, 2, 2, 3, 3 ,3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

# 12
a = b = [1, 2, 3]
a[1] = 4
print(a, b)
print('=-' * 50 + '=')


# ======================================== 조 건 문 ========================================

# 파이썬에만 있는 조건방식
if 1 in [1, 2, 3] :
    print('있어')
if 1 in (1, 2, 3) :
    print('있어')
if 'j' in 'jkd' :
    print('있어')
if 1 not in [4, 2, 3] :
    print('없어')
if 1 not in (4, 2, 3) :
    print('없어')
if 'j' not in 'akd' :
    print('없어')

# pass - 조건문 안에서 아무것도 안하려면 ?
color = ['black', 'red', 'blue']
if 'green' not in color :
    pass
else :
    print('없다야.')

# elif - 다 아는 그거임
color = ['black', 'red', 'blue']
color2 =['green', 'yellow']
if 'grey' in color :
    pass
elif 'grey' in color2 :
    pass
else :
    print('아무리 찾아봐도 없다야')

# 위에꺼를 3줄로 쓸 수도 있음
if 'grey' in color : pass
elif 'grey' in color2 : pass
else : print('아무리 찾아봐도 없다야')

# 조건부표현식 ***
score = 70
if score >= 60 :
    message = 'success'
else :
    message = 'failure'
print(message)
message = 'success' if score >= 60 else 'failure'  # 결과는 같다.
print(message)

