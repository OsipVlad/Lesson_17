def febonachi(n):
    fib1 = fib2 = 1
    for i in range(2, n):
        print(fib1, end=' ')
        fib1, fib2 = fib2, fib1 + fib2

    return "\n{}".format(fib2, end=' ')

print(febonachi(int(input("to which element to make the calculation: "))))