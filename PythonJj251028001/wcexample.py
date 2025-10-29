import wizcoin

purse = wizcoin.WizCoin(2, 5, 99)
print(purse)
print("G:", purse.galleons, "S:", purse.sickles, "K:", purse.knuts)
print("total value:", purse.value())
print("weight:", purse.weightInGrams(), "grams")

print()

coinJar = wizcoin.WizCoin(13, 0, 0)
print(coinJar)
print("G:", coinJar.galleons, "S:", coinJar.sickles, "K:", coinJar.knuts)
print("total value:", coinJar.value())
print("weight:", coinJar.weightInGrams(), "grams")
