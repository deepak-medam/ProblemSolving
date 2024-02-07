"""
Given a string 'S' print the sum of weight of the String. A weight of character is defined as the ASCII value of corresponding character.

Input Description:
You are given a string ‘s’

Output Description:
Print weight

Sample Input :
abc
Sample Output :
294
"""

################################ Solution ################################
userInput = input()
weight = 0
for letter in userInput:
    weight += ord(letter)

print(weight)