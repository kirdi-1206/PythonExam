# 점프 투 파이썬 80page

# 리스트 관련 함수

# append - 리스트 add
a = [1, 2, 3]
a.append(4)
print(a)
print('=' * 50)

# sort - 리스트 정렬
a = [1, 4, 3, 2]
a.sort()
print(a)
print('=' * 50)

# reverce - 리스트 뒤집기
a = [1, 4, 2, 3]
a.reverse()
print(a)
print('=' * 50)

# index - 해당 값의 위치 
a = [1, 4, 2, 3]
print(a.index(3))  # 0부터 센다.
# print(a.index(5))  # 요소에 없는 값을 넣으면 ValueError: 5 is not in list 에러 발생
print('=' * 50)

# insert - 리스트 삽입
a = [1, 4, 2, 3]
a.insert(0, 5)  # insert(위치, 값)
print(a)
print('=' * 50)

# remove - 리스트 제거
a = [1, 4, 2, 3]
a.remove(3)
print(a)
# a.remove(3) # 리스트 범위 안에 없는 것 제거 시 ValueError: list.remove(x): x not in list 에러 발생
print(a)
print('=' * 50)

# 리스트 요소 출력 후 삭제
a = [1, 4, 2, 3]
print(a.pop(0))
print(a)
print('=' * 50)

# 리스트 요소 개수
a = [1, 4, 2, 3, 1]
print(len(a))     # 전체 요소의 개수
print(a.count(1)) # 값이 1인 요소의 개수
print('=' * 50)

b = [3, 5]
# print(a * b)  # 행렬처럼 곱해질것 같지만 안됌

# ============================== 튜플 자료형 ==============================
# 튜플은 값의 생성, 수정, 삭제가 불가능 하다
# 튜플의 형태
t1 = ()
t2 = (1,)      # 요소가 1개이면 ','를 붙혀줘야한다.
t3 = (1, 2, 3)
t4 = 1, 2, 3   # '()'를 넣지 않아도 된다.
t5 = ('a', 'b', ('ab', 'cd'))
t6 = 'a', 'b', ('ab', 'cd')

t1 = (1, 2, 'a', 'b')
# del t1[0]   # TypeError: 'tuple' object doesn't support item deletion 발생
# t1[0] = 'c' # TypeError: 'tuple' object does not support item assignment 발생

print(t1)
print(t1[1:])
t2 = (3, 4)
print(t1 + t2)
# print(t1 * t2) 이건 안됌

# len 튜플의 길이
print(len(t1))
print('=' * 50)

# 나혼자 코딩87p
print((1, 2, 3) + (4,))
print('=' * 50)

# ============================== 딕셔너리 자료형 ==============================
"""
대응 관계를 나타내는 자료형
{Key1 : Value1, Key2: Value2, Key3 : Value3, ...}

"""
dic = {'name' : 'Kim', 'phone' : '010-1234-5678', 'birth' : '1995-12-08'}
print(dic)
a = {1 : 'hi'}
print(a)
b = {'a' : [1, 2, 3]}
print(b)
print('=' * 50)

# 딕셔너리 쌍 추가
a = {1: 'a'}
a[2] = 'b' # {2: 'b'} 쌍 추가
print(a)
a['name'] = 'pey' # {'name', 'pey} 인 쌍 추가
print(a)
print('=' * 50)

# 딕셔너리 삭제    ----------그럼 n번째 딕셔너리 요소는 어떻게 삭제하나 ????
del a[2] # Key가 2인 쌍 삭제
print(a)
print('=' * 50)
t1 = {'a' : 2, 'b' : 5, 'c' : 7}
# del[t1[0]] # 키에 없으면 KeyError: 0 발생
print(t1) 
print('=' * 50)

# t1 = {1 : 2 : 3, 4 : 5 : 6} # 대응이 3개인건 안됌

# Key 를 사용해 Value를 얻기
grade = {'pey' : 10, 'julliet' : 12}
print(grade['pey'])
print('=' * 50)
# 딕셔너리에서는 인덱싱 방법을 사용할 수 없다.

# 딕셔너리의 Key가 중복되면
a = {1 : 'a', 1 : 'b'}
print(a) # (1 : 'a') 가 무시됨
print('=' * 50)

# 딕셔너리의 Key 리스트
a = {'name' : 'Kim', 'phone' : '010-1234-5678', 'birth' : '1995-12-08'}
aKeys = a.keys() # 리스트와 같지만 insert, appent, remove, pop, 수정 불가능
print(aKeys)
aKeyList = list(aKeys)
print(aKeyList) # 이렇게 하면 a 의 Key 리스트와 같은 요소를 가지고 있는 list형 변수가 된다.
print('=' * 50)

# 딕셔너리의 Value 리스트
aValues = a.values()
print(aValues)
aValueList = list(aValues)
print(aValueList)
print('=' * 50)

# 딕셔너리의 Key, Value 쌍으로 얻기
aItems = a.items()
print(aItems)
# aItems.append(['gender', 'female']) # 마찬가지로 여기서 바로 append 못함
aItemList = list(aItems)
aItemList.append(['gender', 'female']) # 여기서는 추가 가능
print(aItemList)
print('=' * 50)

# Key, Value 쌍 모두 지우기
a.clear()  # 전체 삭제
print(a)
a = {'name' : 'Kim', 'phone' : '010-1234-5678', 'birth' : '1995-12-08'}

# get - Key로 Value 얻기
print(a.get('name'))
print(a.get('job'))  # 없으면 None : False
# print(a['job'])      # 없으면 KeyError: 'job'

if not a.get('job') :
    print('Key : ''job''은 없다.')

print(a.get('job', 'default')) # get의 리턴이 none인 경우 뒤엣 값을 반환 한다.

# 특정 값이 있는지 반환한다.
print('name' in a) # True
print('job' in a)  # False
print('=' * 50)

# ============================== 집합 자료형 ==============================
# set 은 중복 X , 순서가 없음
s1 = set([1, 3, 2])
print(s1)
s2 = set('Hello')
print(s2)
print('=' * 50)

# list형으로 변환 가능
l1 = list(s1)
l2 = list(s2)
print(l1)
print(l2)
print('=' * 50)

# 교집합, 차집합, 합집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

print(s2 - s1)
print(s2.difference(s1))
print('=' * 50)

# add - 집합 값 추가
s1.add(7)
s1.add(4) # 중복 값 추가해도 변화 X
print(s1)

# update 값 여러개 추가
s1.update([8, 9, 10])
print(s1)
"""
s1.add([1, 2, 3])  # set에 이런 짓은 안됌
print(s1)
"""

# remove - 특정 값 제거
s1.remove(10)
print(s1)
# s1.remove(10) # 없는거 제거하려고 하면 KeyError: 10 에러 뜸
# s1.remove(9, 8, 7) # 여러개 삭제도 안됌 ~
print('=' * 50)

# ============================== 불(Bool) 자료형 ==============================
a = True
b = False
print(type(a))
print(type(b))
print('=' * 50)

print(1 == 1)
print(2 >= 1)
print(2 <= 1)
print('=' * 50)

print(bool('python'))   # True   : string
print(bool(''))         # False  : string
print(bool([1, 2, 3]))  # True   : list
print(bool([]))         # False  : list
print(bool((1, 2, 3)))  # True   : 튜플
print(bool(()))         # False  : 튜플
print(bool({1 : 'a'}))  # True   : 딕셔너리
print(bool({}))         # False  : 딕셔너리
print(bool(1))          # True   : 숫자 (0이 아니면 True)
print(bool(0))          # False  : 숫자
dic = {'a' : 1}
print(bool(dic.get('b'))) # False : 딕셔너리의 None



# Bool의 활용
a = [1, 2, 3, 4]
while a :
    print(a.pop())

# 106 페이지까지 완료