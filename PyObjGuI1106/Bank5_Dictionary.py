accountsList = []


def newAccount(name, balance, password):
    global accountsList
    newAccountDict = {"name": name, "balance": balance, "password": password}
    accountsList.append(newAccountDict)


def show(accountNumber):
    global accountsList
    print("Account", accountNumber)
    thisAccountDict = accountsList[accountNumber]
    print("     名字", thisAccountDict["name"])
    print("     余额", thisAccountDict["balance"])
    print("     密码", thisAccountDict["password"])
    print()


def getBalance(accountNumber, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict["password"]:
        print("不正确的密码")
        return None
    return thisAccountDict["balance"]


def deposit(accountNumber, amountToDeposit, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if amountToDeposit < 0:
        print("你不能存负数！")
        return None
    elif password != thisAccountDict["password"]:
        print("不正确的密码")
        return None
    thisAccountDict["balance"] += amountToDeposit
    return thisAccountDict["balance"]


def withdraw(accountNumber, amountToWithdraw, password):
    global thisAccountDict
    thisAccountDict = accountsList[accountNumber]
    if amountToWithdraw < 0:
        print("您不能提取负金额!")
        return None
    elif password != thisAccountDict["password"]:
        print("此帐户的密码不正确")
        return None
    elif amountToWithdraw > thisAccountDict["balance"]:
        print("你取的钱比你账户里的钱还多")
        return None
    thisAccountDict["balance"] -= amountToWithdraw
    return thisAccountDict["balance"]


print("Joe's account is account number:", len(accountsList))
newAccount("Joe", 100, "soup")
print("Mary's account is account number:", len(accountsList))
newAccount("Mary", 12345, "nuts")

while True:
    print()
    print("按b键获取余额")

    print("按d键进行存款")

    print("按n创建新帐户")

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
            print("你的新余额是:", newBalance)

    elif action == "n":
        print("新帐户")
        userName = input("你叫什么名字？ ")
        userStartingAmount = int(input("您的首次存款金额是多少？ "))
        userPassword = input("您想为这个帐户使用什么密码？ ")

        userAccountNumber = len(accountsList)
        useraccount = newAccount(userName, userStartingAmount, userPassword)
        print("您的新帐号是:", userAccountNumber)
print("Done")
