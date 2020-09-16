import re


def isvalid_variable_name(sentence):
    ''' returns a list of errors '''
    errors = []

    # get first letter and check if firstLetter is a digit
    firstLetter = sentence[0]

    if firstLetter.isdigit():
        errors.append(
            'First letter is a digit and would not be a valid variable name')

    for character in sentence:
        if not (character.isalnum() or character == '_'):
            errors.append(
                'Variables can only contain letters numbers and underscores')
    return errors


def camelcase(sentence):
    # title cased and joined together
    answer = ''.join(sentence.lower().title().split())
    try:
        # get first letter and lowercase
        firstLetter = answer[0].lower()

        # put the pieces back together
        return firstLetter + answer[1:]
    except IndexError:
        return ''


def removeSpecialCharacters(sentence):
    # regex of only not underscore, letters and numbers
    regex = '[^A-Za-z0-9_]+'
    return re.sub(regex, '', sentence)


def main():
    question = 'Enter a sentence to camel case: '
    answer = input(question)
    camelcased = removeSpecialCharacters(camelcase(answer))
    print(camelcased)
    errors = isvalid_variable_name(camelcased)
    print(*errors, sep="\n")


if __name__ == "__main__":
    main()
