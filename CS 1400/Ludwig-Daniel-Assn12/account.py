class Account:
    def __init__(self, id=0, balance=100, annualInterestRate=0):
        self.__id = id
        self.__balance = balance
        self.__annual_interest_rate = annualInterestRate

    def getId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getAnnualInterestRate(self):
        return self.__annual_interest_rate

    def getMonthlyInterestRate(self):
        return self.__annual_interest_rate / 12

    def getMonthlyInterest(self):
        return (self.getMonthlyInterestRate() / 100) * self.__balance

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount
