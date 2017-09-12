# __author: Lambert
# __date: 2017/9/12 11:04
li = []
for i in range(1000):
    li.append(i)


class pagenation:
    def __init__(self, page):
        try:
            p = int(page)
        except Exception as err:
            p = 1
        self.page = p

    @property
    def start_page(self):
        return (self.page - 1) * 10

    @property
    def end_page(self):
        return self.page * 10


while True:
    page = input('请输入当前页码>>>')
    obj = pagenation(page)
    print(li[obj.start_page:obj.end_page])  # 将start_page 和 end_page伪装为字段
