def GCD(a, b):
    """

    :param a: 
    :param b: 

    """
    # code here
    if b == 0:
        return a
    return GCD(b, a % b)
