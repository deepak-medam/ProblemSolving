s1 = "ABCD"
s2 = "AC"

################################ Method 01 #################################


def isSubSequence(s1, s2):
    index = 0
    for char in s1:
        if char == s2[index]:
            index += 1
            if index == len(s2):
                print("True")
                break


################################ Method 02 #################################
def isSubSeq(S1, S2):
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            j += 1
        i += 1
    if j == len(s2):
        return True
    else:
        return False


print(isSubSeq(s1, s2))

################################ Method 03 #################################


def isSubSeq(s1, s2, m, n):
    if n == 0:
        return True
    if m == 0:
        return False
    if s1[n - 1] == s2[m - 1]:
        return isSubSeq(s1, s2, m - 1, n - 1)
    else:
        return isSubSeq(s1, s2, m - 1, n)
