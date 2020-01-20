import sys, collections

# 파이썬으로는 어떻게 구조체를 만드는 지 ... 날 구조해줬으면....
# 나는 영어공부를 하고 있는데 현재 / 과거 / 과거분사를 외우기가 너무 힘들었다.
# 그래서 외우기 좋은 프로그램을 만들려고 한다. 파이썬으로!!

# NPPItem = collections.namedtuple('index', ['Now', 'Past', 'P.P'])
# NPPItem1 = NPPItem('am/is/are', 'was/were', 'been')
# print(NPPItem1)

Employee = collections.namedtuple('Person', ['name', 'id'])    # 리스트로 써도 되고!
employee1 = Employee('Dave', '4011')
print (employee1)
print (type(employee1))

class NPPItem:
    def __init__(self, now, past, pp):
        self.now = now
        self.past = past
        self.pp = pp

NPPItem1 = NPPItem('am/is/are', 'was,were', 'been')
print(NPPItem1.now, NPPItem1.past, NPPItem1.pp)

