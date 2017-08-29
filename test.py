def foo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    a = 1
    b = 1
    c = 0
    for i in range(n - 1):
        #     c = a + b
        #     a = b
        #     b = c
        # return c
        a, b = b, a + b
    return b


for i in range(10):
    print(foo(i))
