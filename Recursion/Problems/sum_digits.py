def sumDigits(n):
    """

    :param n:

    """
    if n < 10:
        return n
    return sumDigits(n // 10) + n % 10


print(sumDigits(99999))
