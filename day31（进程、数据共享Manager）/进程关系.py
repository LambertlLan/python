# __author: Lambert
# __date: 2017/9/21 11:54
import os


def info(tittle):
    print(tittle)
    print('module name', __name__)  # module name __main__
    print('parent process:', os.getppid())  # parent process: 17516
    print('process id:', os.getpid())  # process id: 17772


if __name__ == '__main__':
    info('process line')
