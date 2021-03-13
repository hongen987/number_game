import random
x = random.randint(1,100)
while True:
    y = input('請輸入從1~100的其中一個數字')
    y = int(y)
    if y == x:
        print('你猜對了')
        break
    else:
        if x >= y and y >= 1: 
            print('比這個數字大')
        elif x <= y and y <= 100:
            print('比這個數字小')
        else:
            print('只能輸入1~100的數')