def fib(n):
    a, b, c = 0, 1, 1
    for _ in range(n):
        print(a, end = ' ')
        a, b, c = b, c, a+b+c

n = int(input("Enter Terms: "))
fib(n)





