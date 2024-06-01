def nCr(n, r):
    # code here
    if r == 0 or r == n:
        return 1

    return nCr(n - 1, r - 1) + nCr(n - 1, r)
