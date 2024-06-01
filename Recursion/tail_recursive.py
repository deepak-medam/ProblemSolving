#  tail recursive
def fun(n):
    if n<=0:
        return
    print(n, end=" ")
    fun(n-1)

def fun(n):
    while n!=0:
        print(n, end=" ")
        n = n-1

# not tail recursive
def fun_1(n):
    if n<=0:
        return
    fun_1(n-1)
    print(n, end=" ")

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)