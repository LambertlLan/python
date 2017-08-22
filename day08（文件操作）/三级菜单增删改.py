# __author: Lambert
# __date: 2017/8/21 16:23
father_layer = []
with open('json','r',encoding='utf-8') as file:
    dic = eval(file.read())
    dic_layer = dic
    while True:
        for key in dic_layer:
            print(key)
        choice = input('q:返回上一层,exit:退出,a:新增,d:删除,e:修改\n输入名字进入下一级>>>')
        if choice == 'q':
            dic_layer = father_layer.pop()
            continue
        elif choice == 'exit':
            break
        elif choice == 'a':
            add = input('请输入要新增的内容>>>')
            dic_layer.setdefault(add,{})
            continue
        else:
            if dic_layer[choice]:
                father_layer.append(dic_layer)
            else:
                add_choice = input('输入新增数据>>>')
                dic_layer[choice].setdefault(add_choice,{})
                father_layer.append(dic_layer[choice])
            dic_layer = dic_layer[choice]
