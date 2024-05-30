user_input = input("Enter the string to check if it's a palindrome: ")

################################ Method 01 #################################
def isPalindrome(s1):
    s2 = s1[::-1]
    if s1 == s2:
        return True
    else:
        return False


print(isPalindrome(user_input))

################################ Method 02 #################################
def isPalindrome_(s1):
    low = 0
    high = len(s1)-1
    while low < high:
        if s1[low] != s1[high]:
            print("No")
            break
        low += 1
        high -= 1
    else:
        print("Yes")


isPalindrome_(user_input)