# __author: Lambert
# __date: 2017/9/6 13:58
import shelve

f = shelve.open('SHELVE_TEXT')
f['info'] = {'name': 'tung', 'age': 29}  # 往文件中写入json

print(f['info'])  # 可直接取出json
