# __author: Lambert
# __date: 2017/8/16 15:11
keep_flage = False
for i in range(10):
    print('第%s次' % i)
    for j in range(10):
        print('layer%s' % j)
        if j == 6:
            keep_flage = True
            break
    if keep_flage:
        break