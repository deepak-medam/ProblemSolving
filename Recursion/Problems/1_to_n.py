# Problem 01
def print1toN(n):
    if n == 0:
        return
    print1toN(n-1)
    print(n)

print1toN(4)

# Problem 02
# Print 1 To N Without Loop

# Print numbers from 1 to N without the help of loops.

# Example 1:

# Input:
# N = 10
# Output: 1 2 3 4 5 6 7 8 9 10

# Example 2:

# Input:
# N = 5
# Output: 1 2 3 4 5
 

# Your Task:
# This is a function problem. You only need to complete the function printNos() that takes N as parameter 
# and prints number from 1 to N recursively. Don't print newline, it will be added by the driver code.


# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N) (Recursive).


# Constraints:
# 1 <= N <= 1000

def printNos(self,N):
    #Your code here
    if N == 0:
        return
    self.printNos(N-1)
    print(N, end=" ")