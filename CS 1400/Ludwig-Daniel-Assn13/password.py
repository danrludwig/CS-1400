

import re


class Password:

    def setPassword(self, passGuess):
        self.__passGuess = passGuess
        self.__error = []
        self.__message = ''
        self.__valid = True

    def isValid(self):
        self.__isLength()
        self.__isSpecialCharacters()
        self.__hasdigits()
        self.__containPassword()
        self.__end123()
        return self.__valid

    def __end123(self):
        if self.__passGuess.endswith('123'):
            self.__error.append(5)
            self.__valid = False

    def __containPassword(self):
        if 'password' in self.__passGuess:
            self.__error.append(4)
            self.__valid = False

    def __hasdigits(self):
        num = sum(i.isdigit() for i in self.__passGuess)
        if num < 2:
            self.__error.append(3)
            self.__valid = False
            '''
            learned the method above to count digits from
            https://stackoverflow.com/questions/24878174/how-to-count-digits-letters-spaces-for-a-string-in-python
            '''

    def __isSpecialCharacters(self):
        if not re.match('[A-Za-z0-9]*$', self.__passGuess):
            self.__error.append(2)
            self.__valid = False

    def __isLength(self):
        if len(self.__passGuess) < 8:
            self.__error.append(1)
            self.__valid = False

    def getErrorMessage(self):
        if not self.__valid:
            if 1 in self.__error:
                self.__message += 'must have 8 characters\n'
            if 2 in self.__error:
                self.__message += 'can only have letters and digits\n'
            if 3 in self.__error:
                self.__message += 'must have at least 2 digits\n'
            if 4 in self.__error:
                self.__message += 'cannot contain word "password"\n'
            if 5 in self.__error:
                self.__message += 'cannot end with "123"\n'
            return self.__message
        else:
            pass


