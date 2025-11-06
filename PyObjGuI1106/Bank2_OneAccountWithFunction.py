accountName = ""
accountBalance = 0
accountPassword = ""


def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password


def show():
    global accountName, accountBalance, accountPassword
    print("     名字", accountName)
    print("     余额", accountBalance)
    print("     密码", accountPassword)
    print()


def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print("不正确的密码")
        return None
    return accountBalance


def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print("你不能存负数！")
        return None
    elif password != accountPassword:
        print("不正确的密码")
        return None
    accountBalance += amountToDeposit
    return accountBalance


def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print("您不能提取负金额!")
        return None
    elif password != accountPassword:
        print("此帐户的密码不正确")
        return None
    elif amountToWithdraw > accountBalance:
        print("你取的钱比你账户里的钱还多")
        return None
    accountBalance -= amountToWithdraw
    return accountBalance


newAccount("Joe", 100, "soup")

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
        userPassword = input("请输入密码: ")
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print("你的余额是:", theBalance)

    elif action == "d":
        print("Deposit:")
        userDepositAmount = int(input("请输入存款金额: "))
        userPassword = input("请输入密码: ")
        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print("你的新余额是: ", newBalance)

    elif action == "s":
        print("Show:")
        show()

    elif action == "q":
        break

    elif action == "w":
        print("Withdraw:")

        userWithdrawAmount = int(input("请输入提现金额: "))
        userPassword = input("请输入密码: ")
        newBalance = withdraw(userWithdrawAmount, userPassword)
        if newBalance is not None:
            print("你的新Balance是:", newBalance)
print("Done")
