# Problem 01: Factorial n where n >= 0


def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


# Problem 02: N-th fibonacci number


def fibonacci(num):
    if num == 1 or num == 0:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)
