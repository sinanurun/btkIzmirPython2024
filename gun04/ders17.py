def sayiYazdir(baskan,by="ali",*args):
    print(args)
    print(*args)
    print(type(args))
    print([*args])
    for arg in args:
        print(arg)

sayiYazdir(5,6,98,54,21)