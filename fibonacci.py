def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        c = a + b
        a = b
        b = c

    return b

for x in range(40):
    print(fibonacci(x))