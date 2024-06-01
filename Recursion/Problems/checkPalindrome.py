def isPalindrome(st, start, end):
    if start >= end:
        return True
    return (st[start] == st[end] and isPalindrome(st, start+1, end-1))


print(isPalindrome('abcdba', 0, 4))

# Second version


def isPalRec(st, start, end):
    if start >= end:
        return True
    return (st[start] == st[end] and isPalRec(st, start+1, end-1))


def isPalin(N):
    # code here
    st_n = str(N)
    if len(st_n) == 0:
        return True

    return isPalRec(st_n, 0, len(st_n)-1)
