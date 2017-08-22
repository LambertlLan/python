# __author: Lambert
# __date: 2017/8/21 14:23
import sys, time

for i in range(30):
    # print('#', end='', flush=True)
    sys.stdout.write('#')  # 不加flush会放入缓冲区不会立即显示出来，flush是将缓存区的文件放入内存会写入磁盘
    sys.stdout.flush()
    time.sleep(0.1)
