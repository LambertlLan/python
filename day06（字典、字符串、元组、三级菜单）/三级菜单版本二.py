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
dic_layer = dic
parent_layer = []
while True:
    for key in dic_layer:
        print(key)
    choice = input('>>>')
    if choice == 'exit':
        break
    elif choice == 'q':
        dic_layer = parent_layer.pop()
        continue
    else:
        parent_layer.append(dic_layer)
        dic_layer = dic_layer[choice]

