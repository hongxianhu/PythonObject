account0Name = ""
account0Balance = 0
account0Password = ""
account1Name = ""
account1Balance = 0
account1Password = ""
nAccounts = 0


def newAccount(accountNumber, name, balance, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    if accountNumber == 0:
        account1Name = name
        account0Balance = balance
        account0Password = password
    if accountNumber == 1:
        account1Name = name
        account1Balance = balance
        account1Password = password


def show():
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    if account0Name != "":
        print("Account 0")
        print("     名字", account0Name)
        print("     余额", account0Balance)
        print("     密码", account0Password)
        print()
    if account1Name != "":
        print("Account 1")
        print("     名字", account1Name)
        print("     余额", account1Balance)
        print("     密码", account1Password)
        print()


def getBalance(accountNumber, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    if accountNumber == 0:
        if password != account0Password:
            print("不正确的密码")
            return None
        return account0Balance
    if accountNumber == 1:
        if password != account1Password:
            print("不正确的密码")
            return None
        return account1Balance


def deposit(accountNumber, amountToDeposit, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    if accountNumber == 0:
        if amountToDeposit < 0:
            print("你不能存负数！")
            return None
        elif password != account0Password:
            print("不正确的密码")
            return None
        account0Balance += amountToDeposit
        return account0Balance

    if accountNumber == 1:
        if amountToDeposit < 0:
            print("你不能存负数！")
            return None
        elif password != account1Password:
            print("不正确的密码")
            return None
        account1Balance += amountToDeposit
        return account1Balance


def withdraw(accountNumber, amountToWithdraw, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    if accountNumber == 0:
        if amountToWithdraw < 0:
            print("您不能提取负金额!")
            return None
        elif password != account0Password:
            print("此帐户的密码不正确")
            return None
        elif amountToWithdraw > account0Balance:
            print("你取的钱比你账户里的钱还多")
            return None
        account0Balance -= amountToWithdraw
        return account0Balance
    if accountNumber == 1:
        if amountToWithdraw < 0:
            print("您不能提取负金额!")
            return None
        elif password != account1Password:
            print("此帐户的密码不正确")
            return None
        elif amountToWithdraw > account1Balance:
            print("你取的钱比你账户里的钱还多")
            return None
        account1Balance -= amountToWithdraw
        return account1Balance


newAccount(nAccounts, "Joe", 100, "soup")

while True:
    print()
    print("按b键获取余额")

    print("按d键进行存款")

    print("按w键取款")

    print("按s键显示账户")

    print("按q键退出")
    print()

    action = input("你想做什么? ").lower()[0]
    print()
    if action == "b":
        print("Get 余额:")
        nAccounts = input("")
        userPassword = input("请输入密码: ")
        theBalance = getBalance(nAccounts, userPassword)
        if theBalance is not None:
            print("你的余额是:", theBalance)

    elif action == "d":
        print("Deposit:")
        nAccounts = input("")
        userDepositAmount = int(input("请输入存款金额: "))
        userPassword = input("请输入密码: ")
        newBalance = deposit(nAccounts, userDepositAmount, userPassword)
        if newBalance is not None:
            print("你的新余额是: ", newBalance)

    elif action == "s":
        print("Show:")
        show()

    elif action == "q":
        break

    elif action == "w":
        print("Withdraw:")
        nAccounts = input("")
        userWithdrawAmount = int(input("请输入提现金额: "))
        userPassword = input("请输入密码: ")
        newBalance = withdraw(nAccounts, userWithdrawAmount, userPassword)
        if newBalance is not None:
            print("你的新Balance是:", newBalance)
print("Done")
