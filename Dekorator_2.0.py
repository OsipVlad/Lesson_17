
def vvod_args(args):
    def revers(*a, **b):
        return args(*a, **b)
    return revers

@vvod_args
def args(a,b):
    a = str(a)
    b = str(b)
    if a and b == "cat":
        print("NO cat, only Dog's")
        return "try again"
    return b[::-1],a[::-1]



print(vvod_args(args)("dog","horse"))