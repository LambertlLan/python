# __author: Lambert
# __date: 2017/9/6 11:30
import json

dic = {'tung': 'tung'}
f = open('test.json', 'w')
data = json.dumps(dic)
f.write(data)
# data = json.dump(dic,f)  # 等于data = json.dumps(dic) 和 f.write(data)
f.close()