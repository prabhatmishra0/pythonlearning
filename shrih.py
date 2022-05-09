def fib(n):
    a, b = 0, 1
    print(a, '\n', b)
    while b < n:
        print(b)
        a, b = b, a+b
fib(10)
