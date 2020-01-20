def int_sum(a, b):
    c = a + b
    return c

print('hi I''m human, I have ', 4, ' legs.')

identity = 'human'
legNum = 4
print('hi I''m '+ identity +', I have ', legNum, ' legs.')

a = 10
b = 20
c = a + b
print('1. a + b = ' + str(c))               # 프린트
print('2. a + b = ' + str(int_sum(a, b)))   # 프린트

for i in range(7) :
    if i < 3 :
        print(str(i) + ' : 번째')
    else :
        print(str(i), ' : 번째') # ','로 이을 경우 공백이 자동 추가 된다.

