# This function returns floor of log base 2 n. If you provide n which is power of 2 it will return log base 2n
def fun(n):
    if n <= 1:
        return 0
    else:
        return 1 + fun(n / 2)


print(fun(16))
