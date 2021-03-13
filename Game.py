import random
x = random.randint(1,100)
z = 0
print(x)
while True:
    y = input('請輸入從1~100的其中一個數字')
    y = int(y)
    z = z + 1
    if y == x:
        print('你猜對了')
        print('你猜了', z, '次')
        break
    else:
        if x > y and y >= 1: 
            print('比這個數字大')
        elif x < y and y <= 100:
            print('比這個數字小')
        else:
            print('只能輸入1~100的數')