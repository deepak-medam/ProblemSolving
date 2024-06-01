def printNto1(n):
    """

    :param n: 

    """
    if n <= 0:
        return
    print(n)
    printNto1(n - 1)


printNto1(5)
