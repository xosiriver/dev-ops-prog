import sys

num = int(sys.argv[1])


def fib(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


print(fib(num))
