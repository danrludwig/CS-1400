from password import Password


def main():
    password = Password()
    while True:
        passGuess = input('Enter password: ')
        password.setPassword(passGuess)
        if password.isValid() is True:
            print('Valid Password')
        else:
            print('Invalid Password\n', password.getErrorMessage())
        again = input('Enter "y" to enter another password: ')
        again = again.lower()
        if again == 'y':
            continue
        else:
            break

main()