# bir birini çağıran fonksiyonlar
def birinci():
    print("Birinci Çalıştı")
    return ikinci()

def ikinci():
    print("ikinci çalıştı")
    return ucuncu()

def ucuncu():
    print("ucuncu calisti")
    return 3

if __name__ == '__main__':
    print("hello world")
    a = birinci()
    print(a)