accountName = "Joe"
accountBalance = 100
accountPassword = "soup"

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
        if userPassword != accountPassword:
            print("不正确的密码")
        else:
            print("你的余额是:", accountBalance)

    elif action == "d":
        print("Deposit:")
        userDepositAmount = int(input("请输入存款金额: "))
        userPassword = input("请输入密码: ")

        if userDepositAmount < 0:
            print("你不能存负数！")
        elif userPassword != accountPassword:
            print("不正确的密码")
        else:
            accountBalance += userDepositAmount
            print("你的新余额是: ", accountBalance)

    elif action == "s":
        print("Show:")
        print("     名字", accountName)
        print("     余额", accountBalance)
        print("     密码", accountPassword)
        print()

    elif action == "q":
        break

    elif action == "w":
        print("Withdraw:")

        userWithdrawAmount = int(input("请输入提现金额: "))
        userPassword = input("请输入密码: ")
        if userWithdrawAmount < 0:
            print("您不能提取负金额!")
        elif userPassword != accountPassword:
            print("此帐户的密码不正确")
        elif userWithdrawAmount > accountBalance:
            print("你取的钱比你账户里的钱还多")
        else:
            accountBalance -= userWithdrawAmount
            print("你的新Balance是:", accountBalance)
print("Done")
