# local de bir global değişken tanımlama

def fonksiyon():
    global a
    a = 50
    # arabalar = ["opel"]
    def icinde():
        global b
        b = 100
    icinde()
# print(a)
fonksiyon()
print(a)
print(b)
# print(arabalar)