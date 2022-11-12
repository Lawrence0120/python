# while True:
#     print("1. 蘋果汁 \n2. 柳橙汁 \n3. 葡萄汁 \n4. 系統關閉")
#     a = input("請輸入編號:")
#     if a == '1':
#         print('您選的商品是蘋果汁')
#     elif a == '2':
#         print('您選的商品是柳橙汁')
#     elif a == '3':
#         print('您選的商品是葡萄汁')
#     elif a == '4':
#         print('系統關閉')
#         break
#     else:
#         print("重新輸入")
# import random as r

# print(r.randrange(3))
# print(r.randrange(0, 10, 2))

import random as r

x = r.randrange(0, 101)
while True:
    a = int(input('請輸入1~100的整數:'))
    if a > x:
        print('在小一點')
    elif a < x:
        print('在大一點')
    else:
        print('~恭喜猜中了!!!~')
        break