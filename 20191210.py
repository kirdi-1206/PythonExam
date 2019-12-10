# 점프투 파이썬 130 page


# ============================== while ==============================
# 반복문들은 편의상 주석처리해놓음 각각 주석 풀어서 실행해볼것

MAX_TREE_HIT = 10
treeHit = 0
# while treeHit < MAX_TREE_HIT:
#     treeHit = treeHit + 1
#     print('나무를', str(treeHit),'번 찍었습니다.')
#     if treeHit == MAX_TREE_HIT :
#         print('나무 넘어갑니다.')


# input
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number : """
# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())

# break!

# while True:
    # if int(input('Enter number: ')) == 1: break  # break 됨

# continue
# number = 0
# while number < 10:
#     number = number + 1
#     if number % 2 == 0: continue
#     print(number)

# ============================== for ==============================

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
print('=' * 50)

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)  # 리스트에 들어있는 튜플 앞 뒤 값의 합
print('=' * 50)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print('%d번 학생은 합격입니다.'%number)
    else:
        print('%d번 학생은 불합격입니다.'%number)
print('=' * 50)

# continue
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print('%d번 학생은 합격입니다.'%number)
print('=' * 50)

# range
a = range(10)
print(a)
print(list(a))
b = range(10, 1)      # 난 역순으로 하고 싶었다... 그러나
print(b)
print(list(b))        # 소용 없다...
b = range(10, 0, -1)  # 하지만! 이렇게 하면 된다!! 와! 신기!
print(b)
print(list(b))        
sum = 0
for i in a:
    sum = sum + i
    print(sum)
sum = 0
print('=' * 50)
for i in b:
    sum = sum + i
    print(sum)
print('=' * 50)

# range를 이용한 리스트 활용 for문
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] >= 60:
        print('%d번 학생은 합격입니다.'%number)
    else:
        print('%d번 학생은 불합격입니다.'%number)
print('=' * 50)

# for와 range를 이용한 구구단. 세정찡...
for i in range(2, 10):
    for j in range(1, 10):
        print('%d * %d = %d' %(i, j, i * j), end=' ')  # end는 print의 끝문자를 엔터 말고 다른 글자로 하기 원할 때 쓰는 것
    print('')
print('=' * 50)

# ===== 리스트내포 =====
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
print(result)
print('=' * 50)
# 위 코드를 아래와 같이 바꿀 수 있다.
result = []
print(result)
result = [num * 3 for num in a]
print(result)
print('=' * 50)

# 짝수만 담고 싶다면...
result = [num * 3 for num in a if num % 2 == 0]  # 이 코드에서 result = []로 초기화 시켜주기 때문에 따로 초기화가 필요 없다.
print(result)
print('=' * 50)

# for문을 여러개 사용하는 것도 가능하다.
result = [x * y for x in range(2, 10) for y in range(1, 10)]
print(result)
print('=' * 50)

# 연습문제는 다음꺼에서...