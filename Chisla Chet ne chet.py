def chisla(a):
    index = 0
    chetnie = 0
    nechetnie = 0
    for i in range(0, len(a)):
        chislo = int(a[index])
        c = chislo % 2
        index += 1
        if c == 0:
            chetnie += 1
        else:
            nechetnie += 1
    return "In this number {} even numbers and {} odd numbers".format(chetnie, nechetnie)

print(chisla(input("enter your number: ")))
