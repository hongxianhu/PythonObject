import wizcoin

print(str(type(41)))
print(type(41).__qualname__)

te=wizcoin.WizCoin(1,2,3)
print(type(te).__qualname__)

#  __qualname__特性常用来覆盖__repr__方法