# __author: Lambert
# __date: 2017/8/16 17:11
salary = int(input('salary:'))
msg = '''
1.  iphone6s  5800
2.  mac book    9000
3.  coffee      32
4.  python book    80
5.  bicycle         1500
'''
print(msg)
goods = ['iphone6s', 'mac book', 'coffee', 'python book', 'bicycle']
price = [5800, 9000, 32, 80, 1500]
cart = []
total_price = 0
while True:
    number = input('请输入编号购买:')
    if number == 'q':
        print('您已购买以下商品：')
        for v,j in enumerate(cart):
            print(v,'.',j)
        break
    else:
        number = int(number)
        less_money = salary - price[number - 1]
        if less_money < 0:
            print('余额不足，还差%s' % -less_money)
        else:
            cart.append(goods[number - 1] +':'+ str(price[number - 1]))
            salary = salary - price[number - 1]
            print('已加入购物车')
