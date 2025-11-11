from Account import *


class Bank:
    def __init__(self):
        self.accountsDict = {}
        self.nextAccountNumber = 0

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        self.nextAccountNumber += 1
        return newAccountNumber

    def openAccount(self):
        print("新帐户")
        userName = input("你叫什么名字？ ")
        userStartingAmount = int(input("您的首次存款金额是多少？ "))
        userPassword = input("您想为这个帐户使用什么密码？ ")
        userAccountNumber = self.createAccount(
            userName, userStartingAmount, userPassword
        )
        print("您的新帐号是:", userAccountNumber)
        print()

    def closeAccount(self):
        userAccountNumber = int(input("请输入您的帐号: "))
        userPassword = input("请输入密码: ")
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)
        if theBalance is not None:
            print("你的新余额是: ", theBalance)
            del self.accountsDict[userAccountNumber]

    def balance(self):
        print("Get 余额:")
        userAccountNumber = int(input("请输入您的帐号: "))
        userPassword = input("请输入密码: ")
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)
        if theBalance is not None:
            print("你的余额是:", theBalance)

    def deposit(self):
        print("Deposit:")
        userAccountNumber = int(input("请输入您的帐号: "))
        userDepositAmount = int(input("请输入存款金额: "))
        userPassword = input("请输入密码: ")
        oAccount = self.accountsDict[userAccountNumber]
        newBalance = oAccount.deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print("你的新余额是: ", newBalance)

    def show(self):
        print("Show:")
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            oAccount.show()

    def withdraw(self):
        print("Withdraw:")
        userAccountNumber = int(input("请输入您的帐号: "))
        userWithdrawAmount = int(input("请输入提现金额: "))
        userPassword = input("请输入密码: ")
        oAccount = self.accountsDict[userAccountNumber]
        newBalance = oAccount.withdraw(userWithdrawAmount, userPassword)
        if newBalance is not None:
            print("你的新余额是:", newBalance)
