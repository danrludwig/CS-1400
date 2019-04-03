from account import Account


def printMenu():
    print('(1): Display ID')
    print('(2): Display Balance')
    print('(3): Display Annual Interest Rate')
    print('(4): Display Monthly Interest Rate')
    print('(5): Display Monthly Interest')
    print('(6): Withdraw Money')
    print('(7): Deposit Money')
    print('(8): Exit ')

def main():
    done = False
    complete = False

    negativeId = True
    while negativeId:
        id = int(input('Enter id Number: ') or 0)
        if id < 0:
            print('Can\'t be a negative number.')
        else:
            negativeId = False

    negativeBalance = True
    while negativeBalance:
        balance = float(input('Enter balance number: ') or 100)
        if balance < 0:
            print('Can\'t be a negative number.')
        else:
            negativeBalance = False

    while not complete:
        annualInterestRate = float(input('Enter annual interest rate: ') or 0)
        if annualInterestRate >= 10:
            print('Annual interest rate needs to be less than 10%.')
        elif annualInterestRate < 0:
            print('Can\'t be a negative number.')
        else:
            complete = True


    account = Account(id, balance, annualInterestRate)

    while not done:
        printMenu()
        action = int(input('Action: '))
        if action <= 0:
            print('Invalid number.')
        if action == 1:
            print('ID:', account.getId())
        if action == 2:
            print('Balance:', account.getBalance())
        if action == 3:
            print('Annual Interest Rate:', account.getAnnualInterestRate())
        if action == 4:
            print('Monthly Interst Rate:', account.getMonthlyInterestRate())
        if action == 5:
            print('Monthly Interest:', account.getMonthlyInterest())
        if action == 6:
            amount = float(input('Withdraw amount: '))
            account.withdraw(amount)
        if action == 7:
            amount = float(input('Deposit amount: '))
            account.deposit(amount)
        if action == 8:
            done = True
        if action > 8:
            print('Invalid number.')


main()