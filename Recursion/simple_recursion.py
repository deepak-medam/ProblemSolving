def fun(count):
    """

    :param count:

    """
    if count == 0:
        return
    print("Recursion is fun.")
    fun(count - 1)


fun(5)
