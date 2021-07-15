chislo = int(input("Введите натуральое число: "))
stepen = int(input("Введите показатель степени: "))
stepen_min = 0
for i in range(stepen_min , stepen + 1):
    if stepen > chislo:
        print("Введена степень больше числа, ОШИБКА!")
        break
    b = chislo**stepen_min
    a = f"число {chislo} в {stepen_min}-й степени = {b}\n"
    stepen_min += 1
    print(a)