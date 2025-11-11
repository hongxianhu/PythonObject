from Bank import *

oBank = Bank()

joesAccountNumber = oBank.createAccount("Joe", 100, "JoesPassword")
print("Joe's account number is:", joesAccountNumber)

marysAccountNumber = oBank.createAccount("Mary", 12345, "MarysPassword")
print("Mary's account number is:", marysAccountNumber)

while True:
    print()
    print("按b键获取余额")
    print("按d键进行存款")
    print("To close an account, press c")
    print("按o创建新帐户")
    print("按w键取款")
    print("按s键显示账户")
    print("按q键退出")
    print()

    action = input("你想做什么? ").lower()[0]
    print()
    if action == "b":
        oBank.balance()

    elif action == "c":
        oBank.closeAccount()

    elif action == "d":
        oBank.deposit()

    elif action == "s":
        oBank.show()

    elif action == "q":
        break

    elif action == "w":
        oBank.withdraw()

    elif action == "o":
        oBank.openAccount()

    else:
        print("Sorry, that was not a valid action. Please try again.")

print("Done")
