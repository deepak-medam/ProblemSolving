"""
Given a string S, print 'yes' if it has a vowel in it else print 'no'.
Sample Testcase :
INPUT
codekata
OUTPUT
yes
"""
user_input = input()

vowels = ['a', 'e', 'i', 'o', 'u']
status = 'no'
for char in user_input:
  if char in vowels:
      status = 'yes'
      break
  else:
      status = 'no'

print(status)