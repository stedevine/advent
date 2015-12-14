import string
class Password:
    letters = string.ascii_lowercase
    def nextLetter(letter):
        if (letter == 'z'):
            return 'a'
        return Password.letters[Password.letters.index(letter) + 1]

    def incrementRecursive(oldPassword, endIndex):
        if (endIndex < 0):
            return "".join(oldPassword)

        value = list(oldPassword)
        if (value[endIndex] == 'z') :
            value[endIndex] = 'a'
            return Password.incrementRecursive(value, endIndex -1)

        value[endIndex] = Password.nextLetter(value[endIndex])
        return "".join(value)

    def increment(oldPassword):
        return Password.incrementRecursive(oldPassword, len(oldPassword) - 1)

    def hasIncreasingStraightOfThreeRecursive(password, index):
        if (index > len(password) -3):
            return False

        if (password[index] == 'y' or password[index] == 'z') or not (Password.nextLetter(Password.nextLetter(password[index])) == Password.nextLetter(password[index + 1]) and Password.nextLetter(password[index + 1]) == password[index+2]):
            return Password.hasIncreasingStraightOfThreeRecursive(password, index + 1)

        return True

    def hasIncreasingStraightOfThree(password):
        return Password.hasIncreasingStraightOfThreeRecursive(password, 0)

    def containsInvalidCharacter(password):
        value = list(password)
        return ("i" in value or "o" in value or "l" in value)

    def containTwoPairsOfLetters(password):
        index = 0
        firstPairLetter = ""
        while index < len(password) - 3:
            if (password[index] == password[index+1]):
                firstPairLetter = password[index]
                index += 2
                break
            index += 1

        while index < len(password) - 1 and not firstPairLetter == "":
            if (password[index] == password[index+1] and not password[index] == firstPairLetter):
                return True
            index += 1

        return False

    def isValid(password):
        return Password.hasIncreasingStraightOfThree(password) and Password.containTwoPairsOfLetters(password) and not Password.containsInvalidCharacter(password)

    def getNextPassword(password):
        value = Password.increment(password)
        while not Password.isValid(value):
            print(value)
            value = Password.increment(value)

        return value
