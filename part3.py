import re

sentence = 'Enter a sentence to camel case: '
answer = input(sentence).lower()
# title cased and joined together
answer = ''.join(answer.title().split())

# get first letter and lowercase
firstLetter = answer[0].lower()

# check if firstLetter is a digit
if firstLetter.isdigit():
  print('first letter is a digit and would not be a valid variable name')

for character in answer:
   if not (character.isalnum() or character == '_'):
    print('variables can only contain letters numbers and underscores')

#print all together
print(firstLetter + answer[1:])