N = 100
quanticCoins = 0
walletMultiplication = 0
walletDivision2 = 0
walletDivision4 = 0
f = open("coinModeling4N_3.txt", 'w')

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
    global n, steps, quanticCoins, walletMultiplication, walletDivision2, walletDivision4
    if n % 4 == 0:
        n = int(n / 4)
        walletDivision4 = walletDivision4 + 1
        f.write(f"Кошелек уменьшил в четыре раза кол-во монет до {n}")
        print(f"Кошелек уменьшил в четыре раза кол-во монет до {n}")
        print(f"Кошлек {walletDivision4} раз на четыре поделил кол-во монет.")
    elif n % 4 == 2:
        x = n % 6
        n = n - x
        n = int(n / 6)
        print(f"Кошелек уменьшил вдвое кол-во монет до {n}")
        print(f"Кошлек {walletDivision2} раз на два поделил кол-во монет.")
    else:
        n = n * 3
        walletMultiplication = walletMultiplication + 1
        print(f"Кошелек утроил кол-во монет до {n}")
        print(f"Кошлек {walletMultiplication} раз удвоил кол-во монет.")


def quanticStep():
    takeCoin()
    f.write("Квантик забрал монету.\n")


def process_n():
    while (True):
        if n == 0:
            print(f"Кошелек опустошен за {steps} шагов. Моделирование завершено")
            f.write(f"Шагов:{steps}. Делений пополам:{walletDivision2}. Делений на 4: {walletDivision4}. Утроений:{walletMultiplication}. {n}\n")
            #f.write(f"{walletMultiplication}\n")
            break
        elif n == 1:
            takeCoin()
            continue
        else:
            quanticStep()
            walletStep()

for i in range(1000):
    steps = 0
    quanticCoins = 0
    n = i
    walletMultiplication = 0
    walletDivision2 = 0
    walletDivision4 = 0
    print(f"Исходное кол-во монет в кошельке {n}")
    print("Запускаем моделирование")
    f.write(f"Кол-во:{n}. ")
    process_n()
n = int(input())
f.write(f"Исходное кол-во монет в кошельке {n}. ")
process_n()