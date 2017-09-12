# __author: Lambert
# __date: 2017/9/11 16:06


class BaseRquest:
    def __init__(self):
        print('2BaseRquest.init')


class RquestHandler(BaseRquest):
    def __init__(self):
        print('1RquestHandler.init')
        BaseRquest.__init__(self)

    def serve_forever(self):
        print('3RquestHandler.serve_forever')
        self.process_request()


class Minx:
    def process_request(self):
        print('4Minx.process_request')


class Son(Minx, RquestHandler):
    pass


obj = Son()
obj.serve_forever();
# RquestHandler中的self代指调用者，
# 故执行到self.process_request() = obj.process_request(),
# 然后再Minx中去找process_request方法
