juices = ['蘋果汁', '柳橙汁', '葡萄汁', '可樂', '系統關閉']
while True:
    for i in range(len(juices)):
        print(f'{i + 1}. {juices[i]}')
    ans = int(input('請輸入編號:'))
    if ans == len(juices):
        print("~~系統關閉~~")
        break
    elif ans > len(juices) or ans <= 0:
        print("輸入錯誤查無果汁，請重新輸入")
    else:
        print(f"您點的商品是{juices[ans-1]}")

# import random as r

# print(r.randrange(3))
# print(r.randrange(0, 10, 2))

# import random as r

# x = r.randrange(0, 101)
# while True:
#     a = int(input('請輸入1~100的整數:'))
#     if a > x:
#         print('在小一點')
#     elif a < x:
#         print('在大一點')
#     else:
#         print('~恭喜猜中了!!!~')
#         break