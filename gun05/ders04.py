# namespace yani isim uzayı değişken geçerlilik bölgesi kavramı scope
a = 1


def ustFonksiyon():
    print(a)
    b = 2

    def altFonskiyon():
        print(a)
        print(b)
        c = 3

    altFonskiyon()
    # print(c)


ustFonksiyon()
# print(b)
