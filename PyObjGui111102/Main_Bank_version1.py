from Account import *

accountsDict = {}
nextAccountNumber = 0

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
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)
        if theBalance is not None:
            print("你的余额是:", theBalance)

    elif action == "d":
        print("Deposit:")
        userAccountNumber = int(input("请输入您的帐号: "))
        userDepositAmount = int(input("请输入存款金额: "))
        userPassword = input("请输入密码: ")
        oAccount = accountsDict[userAccountNumber]
        newBalance = oAccount.deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print("你的新余额是: ", newBalance)

    elif action == "s":
        print("Show:")
        for userAccountNumber in accountsDict:
            oAccount = accountsDict[userAccountNumber]
            oAccount.show()

    elif action == "q":
        break

    elif action == "w":
        print("Withdraw:")
        userAccountNumber = int(input("请输入您的帐号: "))
        userWithdrawAmount = int(input("请输入提现金额: "))
        userPassword = input("请输入密码: ")
        oAccount = accountsDict[userAccountNumber]
        newBalance = oAccount.withdraw(userWithdrawAmount, userPassword)
        if newBalance is not None:
            print("你的新余额是:", newBalance)

    elif action == "n":
        print("新帐户")
        userName = input("你叫什么名字？ ")
        userStartingAmount = int(input("您的首次存款金额是多少？ "))
        userPassword = input("您想为这个帐户使用什么密码？ ")
        oAccount = Account(userName, userStartingAmount, userPassword)
        accountsDict[nextAccountNumber] = oAccount
        print("您的新帐号是:", nextAccountNumber)
        nextAccountNumber += 1

print("Done")
