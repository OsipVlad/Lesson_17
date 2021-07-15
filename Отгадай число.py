import random

print("""Отгадайте число от 1 до 10 за 5 попыток!
                    УДАЧИ!!!
     """)
chislo_user = ()
popitka = 0
popitka_nom = 5
chislo = random.randint(1, 11)
while popitka < 5:
    chislo_user = int(input("Введите ваше число: "))
    popitka += 1
    popitka_nom -= 1
    if chislo == chislo_user:
        break

    if chislo != chislo_user:
        print(f"Увы,но нет.\nОсталось попыток: <{popitka_nom}> \n")

if chislo == chislo_user:
    print(f"Ура, это и вправду число {chislo}!!!\nПоздравляю!\nПопыток до победы: {popitka}")
if chislo != chislo_user:
    print(f"И снова нет.\nПопытки закончились, ты проиграл!")

