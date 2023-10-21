y = 0
z = -1
N = 100
quanticCoins = 0
walletMultiplication5 = 0
walletMultiplication7 = 0
walletDivision6 = 0
walletDivision4 = 0
coinNumbers1 = {-1}
coinNumbers2 = {-1}

def addQuanticCoin():
    global quanticCoins
    quanticCoins = quanticCoins + 1

def removeQuanticCoin():
    global quanticCoins

    if (quanticCoins <= 0):
        print("Пытаемся забрать у квантика монеты,а монет то нету!!!")
        exit(-1)
    quanticCoins = quanticCoins - 1

def takeCoin():
    global n, steps, quanticCoins
    n = n - 1
    steps = steps + 1
    addQuanticCoin()
    print(f"Забираем монету. Монет в кошельке {n}. У квантика {quanticCoins} монет")


def giveCoin():
    global n, steps, quanticCoins
    if quanticCoins > 0:
        n = n + 1
        steps = steps + 1
        removeQuanticCoin()
        print(f"Добавляем монету. Монет в кошельке {n}. У квантика {quanticCoins} монет")
    else:
        takeCoin()


def walletStep():
    global n, steps, quanticCoins, walletMultiplication5, walletDivision6, walletDivision4, walletMultiplication7, y, z
    if n % 6 == 0:
        walletDivision6 = walletDivision6 + 1
        n = int(n / 6)
        print(f"Кошелек уменьшил в 6 раз кол-во монет до {n}")
        print(f"Кошлек {walletDivision6} раз на 6 поделил кол-во монет.")
    elif n % 4 == 2:
        walletDivision6 = walletDivision6 + 1
        n = n - n % 6
        n = int(n / 6)
        print(f"Кошелек уменьшил вдвое кол-во монет до {n}")
        print(f"Кошлек {walletDivision6} раз на 6 поделил кол-во монет.")
    elif n % 4 == 0:
        n = int(n / 4)
        walletDivision4 = walletDivision4 + 1
        print(f"Кошелек уменьшил в четыре раза кол-во монет до {n}")
        print(f"Кошлек {walletDivision4} раз на четыре поделил кол-во монет.")
    elif n % 4 == 1:
        n = n * 5
        walletMultiplication5 = walletMultiplication5 + 1
        print(f"Кошелек умножил на 5 кол-во монет до {n}")
        print(f"Кошлек {walletMultiplication5} раз умножил на 5 кол-во монет.")
    elif n % 4 == 3:
        n = n * 7
        walletMultiplication7 = walletMultiplication7 + 1
        print(f"Кошелек умножил на 7 кол-во монет до {n}")
        print(f"Кошлек {walletMultiplication7} раз умножил на 7 кол-во монет.")

def quanticStep():
    global n, steps, quanticCoins, y, z
    if not n in coinNumbers1:
        coinNumbers1.add(n)
        takeCoin()
    elif not n in coinNumbers2:
        coinNumbers2.add(n)
        giveCoin()
    else:
        exit(-2)



f = open("coinModeling4N.txt", 'w')


def process_n():
    while (True):
        if n == 0:
            print(f"Кошелек опустошен за {steps} шагов. Моделирование завершено")
            f.write(f"Шагов:{steps}. Делений на 6:{walletDivision6}. Делений на 4: {walletDivision4}. Умножений на 5:{walletMultiplication5}. Умножений на 7:{walletMultiplication7}.\n")
            #f.write(f"{walletMultiplication}\n")
            break
        elif n == 1:
            takeCoin()
            continue
        else:
            quanticStep()
            walletStep()
for i in range(N):
    coinNumbers1 = {-1}
    coinNumbers2 = {-1}
    steps = 0
    quanticCoins = 0
    n = i
    walletMultiplication5 = 0
    walletMultiplication7 = 0
    walletDivision6 = 0
    walletDivision4 = 0
    print(f"Исходное кол-во монет в кошельке {n}")
    print("Запускаем моделирование")
    f.write(f"Кол-во:{n}. ")
    process_n()
