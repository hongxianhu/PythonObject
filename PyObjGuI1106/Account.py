class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amountToDeposit, password):
        if amountToDeposit < 0:
            print("你不能存负数！")
            return None
        elif password != self.password:
            print("不正确的密码")
            return None
        self.balance += amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if amountToWithdraw < 0:
            print("您不能提取负金额!")
            return None
        elif password != self.password:
            print("此帐户的密码不正确")
            return None
        elif amountToWithdraw > self.balance:
            print("你取的钱比你账户里的钱还多")
            return None
        self.balance -= amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print("此帐户的密码不正确")
            return None
        return self.balance

    def show(self):
        print("     名字", self.name)
        print("     余额", self.balance)
        print("     密码", self.password)
        print()
