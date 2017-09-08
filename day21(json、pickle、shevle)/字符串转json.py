# __author: Lambert
# __date: 2017/9/6 11:39
import json

f = open('test.json', 'r')

data = f.read()
data = json.loads(data)
# data = json.load(f) # 等于data = f.read() data = json.loads(data)
print(type(data))
print(data['tung'])
