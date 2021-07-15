def bank(summa:int,years:int):
    dollar_2021 = 2.55
    infl = 0.17
    print(f"{summa} BYN || {summa//dollar_2021} USD\n1$ = {dollar_2021}")
    for i in range(0, years):
        summa += summa * 0.1
        dollar_2021 += dollar_2021 * infl
        dollar = summa // dollar_2021
        print("{} BYN || {} USD\n1$ = {}".format(int(summa), int(dollar),round(dollar_2021, 2)))
    return "Удачного вклада :)"
summa = int( input("Введите сумму рублей: "))
yers = int(input("На какой срок: "))

print(bank(summa, yers))

