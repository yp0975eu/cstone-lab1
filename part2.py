classes = []
question = 'What are the names of the programming classes you are taking this semester? Leave blank and press enter to exit. '
answer = 'placeholder' # placeholder needed to enter while loop

while answer != '':
  answer = input(question)
  if (answer != ''):
    classes.append(answer)


def printClasses():
  if (len(classes) == 0):
    print('No classes for you')
  else:
    for className in classes:
      print(className)
  pass

printClasses()