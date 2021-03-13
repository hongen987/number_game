import random
a = input('輸入開始值:')
b = input('輸入結束值:')
a = int(a)
b = int(b)
x = random.randint(a, b)
z = 0
while True:
    y = input('請猜1個數字')
    y = int(y)
    z = z + 1
    if y == x:
        print('你猜對了')
        print('你猜了', z, '次')
        break
    else:
        if x > y and y >= a: 
            print('比這個數字大')
        elif x < y and y <= b:
            print('比這個數字小')
        else:
            print('只能輸入從', a,'到', b, '的其中一個數字')