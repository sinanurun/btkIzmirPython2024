def toplama(a,b):
    return a+b

def cikartma(a,b):
    return a-b

def carpma(a,b):
    return a*b

def karsilama():
    def sayiAl():
        return int(input("bir sayı giriniz"))
    islem = input("+, -, *")
    sayi1 = sayiAl()
    sayi2 = sayiAl()
    match islem:
        case "+":
            print(toplama(sayi1, sayi2))
        case "-":
            print(cikartma(sayi1, sayi2))
        case "*":
            print(carpma(sayi1, sayi2))
        case _:
            print("Hatalı İşlem Girişi Oldu")

if __name__=="__main__":
    karsilama()