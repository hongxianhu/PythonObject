accountNamesList = []
accountBalancesList = []
accountPasswordsList = []


def newAccount(name, balance, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)


def show(accountNumber):
    global accountNamesList, accountBalancesList, accountPasswordsList
    print("Account", accountNumber)
    print("     名字", accountNamesList[accountNumber])
    print("     余额", accountBalancesList[accountNumber])
    print("     密码", accountPasswordsList[accountNumber])
    print()


def getBalance(accountNumber, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print("不正确的密码")
        return None
    return accountBalancesList[accountNumber]


def deposit(accountNumber, amountToDeposit, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if amountToDeposit < 0:
        print("你不能存负数！")
        return None
    elif password != accountPasswordsList[accountNumber]:
        print("不正确的密码")
        return None
    accountBalancesList[accountNumber] += amountToDeposit
    return accountBalancesList[accountNumber]


def withdraw(accountNumber, amountToWithdraw, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if amountToWithdraw < 0:
        print("您不能提取负金额!")
        return None
    elif password != accountPasswordsList[accountNumber]:
        print("此帐户的密码不正确")
        return None
    elif amountToWithdraw > accountBalancesList[accountNumber]:
        print("你取的钱比你账户里的钱还多")
        return None
    accountBalancesList[accountNumber] -= amountToWithdraw
    return accountBalancesList[accountNumber]


print("Joe's account is account number:", len(accountNamesList))
newAccount("Joe", 100, "soup")
print("Mary's account is account number:", len(accountNamesList))
newAccount("Mary", 12345, "nuts")

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
        userAccountNumber = int(input("请输入您的帐号: "))
        userPassword = input("请输入密码: ")
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print("你的余额是:", theBalance)

    elif action == "d":
        print("Deposit:")
        userAccountNumber = int(input("请输入您的帐号: "))
        userDepositAmount = int(input("请输入存款金额: "))
        userPassword = input("请输入密码: ")
        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print("你的新余额是: ", newBalance)

    elif action == "s":
        print("Show:")
        userAccountNumber = int(input("请输入您的帐号: "))
        show(userAccountNumber)

    elif action == "q":
        break

    elif action == "w":
        print("Withdraw:")
        userAccountNumber = int(input("请输入您的帐号: "))
        userWithdrawAmount = int(input("请输入提现金额: "))
        userPassword = input("请输入密码: ")
        newBalance = withdraw(userAccountNumber, userWithdrawAmount, userPassword)
        if newBalance is not None:
            print("你的新Balance是:", newBalance)
print("Done")
