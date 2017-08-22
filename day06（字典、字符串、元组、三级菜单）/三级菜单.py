# __author: Lambert
# __date: 2017/8/18 10:36
dic = {
    '四川省': {
        '成都市': {
            '锦江区',
            '高新区'
        },
        '内江市': {
            '隆昌县'
        }
    },
    '广东省': {
        '广州市': {
            '天河区'
        },
        '珠海市': {
            '中山区'
        }
    }
}
is_exit = False
while not is_exit:
    for key in dic:
        print(key)
    choice1 = input('>>>')
    if choice1 == 'exit':
        break
    while not is_exit:
        for key in dic[choice1]:
            print(key)
        choice2 = input('>>>')
        if choice2 == 'q':
            break
        elif choice2 == 'exit':
            is_exit = True
            break
        while True:
            for key in dic[choice1][choice2]:
                print(key)
            choice3 = input('>>>')
            if choice3 == 'q':
                break
            elif choice3 == 'exit':
                is_exit = True
                break
            else:
                print('到底了')
