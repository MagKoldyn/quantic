## Количество циклов моделирования
N = 100
quanticCoins = 0
walletMultiplication = 0
walletDivision = 0

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
    global n, steps, quanticCoins, walletMultiplication, walletDivision
    if n % 2 == 0:
        n = int(n / 2)
        walletDivision = walletDivision + 1
        print(f"Кошелек уменьшил вдвое кол-во монет до {n}")
        print(f"Кошлек {walletDivision} раз на два поделил кол-во монет.")
    else:
        n = n * 3
        walletMultiplication = walletMultiplication + 1
        print(f"Кошелек утроил кол-во монет до {n}")
        print(f"Кошлек {walletMultiplication} раз удвоил кол-во монет.")


def quanticStep():
    global n, steps, quanticCoins
    if n % 2 == 0:
        takeCoin()
    else:
        if (n - 1) % 4 != 0:
            takeCoin()
        else:
            giveCoin()
f = open("coinModeling2.txt", 'w')


def process_n():
    while (True):
        if n == 0:
            print(f"Кошелек опустошен за {steps} шагов. Моделирование завершено")
            f.write(f"Шагов:{steps}. Делений пополам:{walletDivision}. Утроений:{walletMultiplication}.\n")
            break
        elif n == 1:
            takeCoin()
            continue
        else:
            quanticStep()
            walletStep()

for i in range(N):
    steps = 0
    quanticCoins = 0
    n = i
    walletMultiplication = 0
    walletDivision = 0
    print(f"Исходное кол-во монет в кошельке {n}")
    print("Запускаем моделирование")
    f.write(f"Кол-во:{n}. ")
    process_n()

n = int(input())
f.write(f"Исходное кол-во монет в кошельке {n}. ")
process_n()