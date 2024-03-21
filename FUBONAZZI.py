def fibonacci(n):
    if n < 1:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])

    return fib

n = 50
fib = fibonacci(n)

for i in range(n):
    print(fib[i], end=" ")