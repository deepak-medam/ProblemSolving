def fun(n):
    """

    :param n: 

    """
    if n == 0:
        return
    print(n)
    fun(n - 1)
    print(n)


fun(3)